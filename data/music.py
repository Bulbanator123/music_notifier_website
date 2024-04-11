import datetime
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Music(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'musics'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=True)
    api_content = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    artist_id = sa.Column(sa.Integer, sa.ForeignKey("artists.id"))
    user = orm.relationship("Artist")

