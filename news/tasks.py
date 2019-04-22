from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .grabber import NewsGrabber
from news.helpers.grabber_dicts import news_dict


@shared_task
def run_news_grabber():
    NewsGrabber(**news_dict).process()
