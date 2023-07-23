from sqlalchemy import Sequence

from fattestapi.factory.extensions import db


class BaseModel(db.Model):  # type: ignore[name-defined]
    """Parent model of all models"""

    __abstract__ = True

    id = db.Column("id", db.Integer, Sequence("id", start=1), primary_key=True)
