from marshmallow import Schema, post_load

from fattestapi.httptypes.filtering import FilteringRequest


class BaseFilteringSchema(Schema):
    @post_load
    def to_entity(self, data, **kwargs) -> FilteringRequest:
        return FilteringRequest(**data)
