#!/usr/bin/env python

from os import environ
environ['METAREFRESH_ENV'] = 'development'

from metarefresh import app
from metarefresh.models import db

db.create_all()
app.run('0.0.0.0', 6300, debug=True)
