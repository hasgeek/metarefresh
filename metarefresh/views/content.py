from metarefresh import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', active=1)


@app.route('/take-charge')
def contest():
    return render_template('contest.html', active=1)


