import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Artist(SqlAlchemyBase):
    __tablename__ = 'artists'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)