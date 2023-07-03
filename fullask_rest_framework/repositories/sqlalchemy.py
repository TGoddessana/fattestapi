from abc import ABC, abstractmethod
from functools import wraps
from typing import Generic, List, Optional, Type

from flask_marshmallow.sqla import SQLAlchemyAutoSchema  # type: ignore[import]
from flask_sqlalchemy.query import Query
from sqlalchemy import inspect, select

from fullask_rest_framework.repositories.base import T
from fullask_rest_framework.repositories.crud import CRUDRepositoryABC
from fullask_rest_framework.vo.filtering import FilteringRequest
from fullask_rest_framework.vo.pagination import (PaginationRequest,
                                                  PaginationResponse)
from fullask_rest_framework.vo.sorting import SortingRequest


class SQLAlchemyFullRepository(CRUDRepositoryABC, ABC, Generic[T]):
    """
    The implementation of CRUDRepositoryABC, with SQLAlchemy.
    this implementation has dependency with flask-sqlalchemy's SQLAlchemy object.
    """

    def __init__(self, db):
        self.db = db

    @abstractmethod
    def get_model(self):
        pass

    def save(self, entity: T) -> T:
        self.db.session.add(entity)
        self.db.session.commit()
        self.db.session.refresh(entity)
        return entity

    def save_all(self, entities: List[T]) -> List[T]:
        saved_entities = []
        for entity in entities:
            saved_entity = self.save(entity)
            saved_entities.append(saved_entity)
        return saved_entities

    def read_by_id(self, id: int) -> Optional[T]:
        query_result = self.db.session.get(self.get_model(), id)
        return query_result if query_result else None

    def is_exists_by_id(self, id) -> bool:
        return bool(self.db.session.get(self.get_model(), id))

    def read_all(
        self,
        sorting_request: Optional[SortingRequest] = None,
        filtering_request: Optional[FilteringRequest] = None,
    ) -> List[Optional[T]]:
        query = self._get_base_query()
        if filtering_request:
            query = self._filtering(query=query, filtering_request=filtering_request)
        if sorting_request:
            query = self._sorting(query=query, sorting_request=sorting_request)
        else:
            # if no pagination request, return all results without pagination.
            return [
                query_result
                for query_result in self.db.session.execute(select(self.get_model()))
                .scalars()
                .all()
            ]

    def read_all_with_pagination(
        self,
        pagination_request: PaginationRequest,
        sorting_request: Optional[SortingRequest] = None,
        filtering_request: Optional[FilteringRequest] = None,
    ) -> PaginationResponse[T]:
        query = self._get_base_query()
        if filtering_request:
            query = self._filtering(query=query, filtering_request=filtering_request)
        if sorting_request:
            query = self._sorting(query=query, sorting_request=sorting_request)
        query = query.paginate(
            page=pagination_request.page,
            per_page=pagination_request.per_page,
            error_out=False,
        )
        return PaginationResponse(
            count=query.total,
            next_page=query.next_num,
            previous_page=query.prev_num,
            results=[item for item in query.items],
        )

    def read_all_by_ids(self, ids: List[int]) -> List[Optional[T]]:
        return [self.read_by_id(_id) for _id in ids]

    def count(self) -> int:
        return self.db.session.query(self.get_model()).count()

    def delete_by_id(self, id: int) -> None:
        model_instance = self.db.session.get(self.get_model(), id)
        if model_instance:
            self.db.session.delete(self.db.session.get(self.get_model(), id))
            self.db.session.commit()
        else:
            raise ValueError(f"{self.get_model()} with id {id} not found.")

    def delete(self, entity) -> None:
        model_instance = self.db.session.get(self.get_model(), entity.id)
        if not model_instance:
            raise ValueError(
                f"{self.get_model()} with entity {entity} not found.\n"
                f"make sure the entity instance is stored in database."
            )
        self.db.session.delete(model_instance)
        self.db.session.commit()

    def delete_all_by_ids(self, ids: List[int]) -> None:
        self.db.session.query(self.get_model()).filter(
            self.get_model().id.in_(ids)
        ).delete()

    def delete_all(self) -> None:
        self.get_model().query.delete()

    def _get_base_query(self) -> Query:
        return self.db.session.query(self.get_model())

    def _filtering(self, query: Query, filtering_request: FilteringRequest) -> Query:
        """
        filter the query with filtering_object.
        this is implementation of `or` condition.
        """
        for field, word in vars(filtering_request).items():
            query = query.filter(getattr(self.get_model(), field).ilike(f"%{word}%"))
        return query

    def _sorting(self, query: Query, sorting_request: SortingRequest) -> Query:
        for field, direction in vars(sorting_request).items():
            if direction == "asc":
                query = query.order_by(getattr(self.get_model(), field).asc())
            elif direction == "desc":
                query = query.order_by(getattr(self.get_model(), field).desc())
        return query


def read_by_fields(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        field_name = func.__name__[len("read_by_") :]
        if field_name in kwargs:
            field_value = kwargs[field_name]
        else:
            if len(args) < 1:
                raise ValueError(f"{field_name} argument is missing")
            field_value = args[0]
        query_result = (
            self.get_model().query.filter_by(**{field_name: field_value}).first()
        )
        return query_result if query_result else None

    return wrapper
