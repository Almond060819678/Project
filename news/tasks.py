from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .grabber import NewsGrabber


@shared_task
def run_grabber():
    NewsGrabber().grab_articles()
