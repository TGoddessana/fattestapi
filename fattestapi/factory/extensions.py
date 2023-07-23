from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow  # type: ignore[import]
from flask_migrate import Migrate
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

smorest = Api()
db = SQLAlchemy()
migrate = Migrate(db=db)
cors = CORS()
ma = Marshmallow()
jwt = JWTManager()
