#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Website server for metarefresh.
"""

from flask import Flask
from flask.ext.assets import Environment, Bundle
from baseframe import baseframe, baseframe_js, baseframe_css
#from os import environ
from coaster.app import configure

# First, make an app and config it

app = Flask(__name__, instance_relative_config=True)
configure(app, 'METAREFRESH_ENV')

app.register_blueprint(baseframe)
assets = Environment(app)
js = Bundle(baseframe_js,  'js/leaflet/leaflet.js', 'js/jquery.smooth-scroll.min.js', 'js/metarefresh.js',
    filters='jsmin', output='js/metarefresh-packed.js')
css = Bundle(baseframe_css, 'js/leaflet/leaflet.css', 'css/metarefresh.css', 'css/responsive.css',
    filters='cssmin', output='css/metarefresh-packed.css')
assets.register('js_all', js)
assets.register('css_all', css)

import metarefresh.views
#if environ.get('METAREFRESH_ENV') == 'prod':
#    import metarefresh.loghandler
