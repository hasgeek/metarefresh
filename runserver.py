#!/usr/bin/env python

from metarefresh import app
from os import environ

environ['METAREFRESH_ENV'] = 'dev'
app.config['ASSETS_DEBUG'] = True
app.run('0.0.0.0', 6500, debug=True)
