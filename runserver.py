#!/usr/bin/env python

from metarefresh import app
from metarefresh.models import db
from os import environ

environ['METAREFRESH_ENV'] = 'development'
#app.config['ASSETS_DEBUG'] = True
db.create_all()
app.run('0.0.0.0', 6200, debug=True)
