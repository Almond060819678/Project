from __future__ import absolute_import, unicode_literals
from Project.celery import app
from .grabber import NewsGrabber


@app.task
def run_grabber():
    NewsGrabber().grab_articles()
