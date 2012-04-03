#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Website server for metarefresh.
"""

from flask import Flask
from flaskext.assets import Environment, Bundle
from baseframe import baseframe, baseframe_js, baseframe_css
#from os import environ
from coaster import configureapp

# First, make an app and config it

app = Flask(__name__, instance_relative_config=True)
configureapp(app, 'METAREFRESH_ENV')

app.register_blueprint(baseframe)
assets = Environment(app)
js = Bundle(baseframe_js, 'js/jquery.smooth-scroll.min.js', 'js/metarefresh.js', 'js/leaflet/leaflet.js')
css = Bundle(baseframe_css, 'css/metarefresh.css', 'css/responsive.css', 'js/leaflet/leaflet.css')
assets.register('js_all', js)
assets.register('css_all', css)

import metarefresh.views
#if environ.get('METAREFRESH_ENV') == 'prod':
#    import metarefresh.loghandler
