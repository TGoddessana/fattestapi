from flask_marshmallow import Schema  # type: ignore[import]
from marshmallow import post_load

from fattestapi.httptypes.sorting import SortingRequest
from fattestapi.schemas import fields


class SortingRequestSchema(Schema):
    sort_by = fields.Sorting(
        metadata={
            "description": "The sort condition. It must conform to the format"
            "`fieldname:sortcondition (asc or desc)`."
        }
    )

    @post_load
    def to_entity(self, data, **kwargs) -> SortingRequest:
        data = data.get("sort_by")
        if data:
            return SortingRequest(*data)
        return SortingRequest()
