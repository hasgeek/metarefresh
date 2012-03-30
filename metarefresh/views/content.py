from metarefresh import app
from flask import render_template, redirect, url_for


@app.route('/')
def index():
    return render_template('index.html', active=1)


@app.route('/takecharge')
def contest():
    return render_template('contest.html', active=1)


@app.route('/take-charge')
@app.route('/take-charge.html')
def contest_old_url():
    return redirect(url_for('contest'), code=301)
