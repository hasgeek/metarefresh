from metarefresh import app
from flask import render_template, redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('index2012'), code=302)


@app.route('/2012/')
def index2012():
    return render_template('index.html', active=1)


@app.route('/2012/takecharge')
def contest():
    return render_template('contest.html', active=1)


@app.route('/take-charge')
@app.route('/take-charge.html')
@app.route('/takecharge')
def contest_old_url():
    return redirect(url_for('contest'), code=301)
