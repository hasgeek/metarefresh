# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from metarefresh import app
from coaster.sqlalchemy import BaseMixin, BaseNameMixin
from flask.ext.lastuser.sqlalchemy import UserBase

db = SQLAlchemy(app)


class User(db.Model, UserBase):
    __tablename__ = 'user'
