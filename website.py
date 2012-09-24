import sys
import os, os.path
sys.path.insert(0, os.path.dirname(__file__))
os.environ['METAREFRESH_ENV'] = 'production'
from metarefresh import app as application
