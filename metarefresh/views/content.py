# -*- coding: utf-8 -*-

import json
import urllib2

from metarefresh import app
from flask import render_template, redirect, url_for


schedule = [
    [u'09:00 – 09:45', "Registrations and sign-in"],
    [u'09:45 – 10:00', "Introductions"],
    [u'10:00 – 10:45', 256, 230,   0, 258],
    [u'10:45 – 11:15', "Break"],
    [u'11:15 – 12:00', 247, 241, 234, 233],
    [u'12:00 – 12:45', 245, 251, 276, 240],
    [u'12:45 – 02:00', "Lunch"],
    [u'02:00 – 02:45', 271, 267, 275, 242],
    [u'02:45 – 03:30', 248, 254, 272,  96],
    [u'03:30 – 04:00', "Break"],
    [u'04:00 – 04:45', 281, 243, 239, 278],
    [u'04:45 – 05:30', 282, 264, 266, 280],
    [u'05:30 – 06:00', "Feedback"],
]


@app.route('/')
def index():
    return redirect(url_for('index2012'), code=302)


@app.route('/2012/')
def index2012():
    # Load proposals from JSON feed
    # TODO: Cache this?
    data = json.loads(urllib2.urlopen('http://funnel.hasgeek.com/metarefresh/json').read())
    # Index for dictionary lookup
    proposals = {}
    for p in data['proposals']:
        proposals[p['id']] = p
    return render_template('index.html', active=1, schedule=schedule, proposals=proposals)


@app.route('/2012/takecharge')
def contest():
    return render_template('contest.html', active=1)


@app.route('/take-charge')
@app.route('/take-charge.html')
@app.route('/takecharge')
def contest_old_url():
    return redirect(url_for('contest'), code=301)
