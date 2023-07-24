:py:mod:`fattestapi.repositories.sqlalchemy.sqlalchemy`
=======================================================

.. py:module:: fattestapi.repositories.sqlalchemy.sqlalchemy

.. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SQLAlchemyFullRepository <fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository>`
     - .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository
          :summary:

API
~~~

.. py:class:: SQLAlchemyFullRepository(db: flask_sqlalchemy.SQLAlchemy)
   :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository

   Bases: :py:obj:`fattestapi.repositories.crud.CRUDRepositoryABC`, :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`fattestapi.repositories.base.T`\ ]

   .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository

   .. rubric:: Initialization

   .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.__init__

   .. py:method:: get_model()
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.get_model
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.get_model

   .. py:method:: save(entity: fattestapi.repositories.base.T) -> fattestapi.repositories.base.T
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.save

   .. py:method:: save_all(entities: typing.List[fattestapi.repositories.base.T]) -> typing.List[fattestapi.repositories.base.T]
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.save_all

   .. py:method:: read_by_id(id: int) -> typing.Optional[fattestapi.repositories.base.T]
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.read_by_id

   .. py:method:: is_exists_by_id(id) -> bool
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.is_exists_by_id

   .. py:method:: read_all(pagination_request: typing.Optional[fattestapi.httptypes.pagination.PaginationRequest] = None, sorting_request: typing.Optional[fattestapi.httptypes.sorting.SortingRequest] = None, filtering_request: typing.Optional[fattestapi.httptypes.filtering.FilteringRequest] = None) -> typing.Union[typing.List[typing.Optional[fattestapi.repositories.base.T]] | fattestapi.httptypes.pagination.PaginationResponse[fattestapi.repositories.base.T]]
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.read_all

   .. py:method:: read_all_by_ids(ids: typing.List[int]) -> typing.List[typing.Optional[fattestapi.repositories.base.T]]
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.read_all_by_ids

   .. py:method:: count() -> int
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.count

   .. py:method:: delete_by_id(id: int) -> None
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.delete_by_id

   .. py:method:: delete(entity) -> None
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.delete

   .. py:method:: delete_all_by_ids(ids: typing.List[int]) -> None
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.delete_all_by_ids

   .. py:method:: delete_all() -> None
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository.delete_all

   .. py:method:: _get_base_query() -> flask_sqlalchemy.query.Query
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository._get_base_query

      .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository._get_base_query

   .. py:method:: _filtering(query: flask_sqlalchemy.query.Query, filtering_request: fattestapi.httptypes.filtering.FilteringRequest) -> flask_sqlalchemy.query.Query
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository._filtering

      .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository._filtering

   .. py:method:: _sorting(query: flask_sqlalchemy.query.Query, sorting_request: fattestapi.httptypes.sorting.SortingRequest) -> flask_sqlalchemy.query.Query
      :canonical: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository._sorting

      .. autodoc2-docstring:: fattestapi.repositories.sqlalchemy.sqlalchemy.SQLAlchemyFullRepository._sorting
