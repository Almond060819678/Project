from django.test import TestCase

from news.grabber import NewsGrabber
from news.helpers.grabber_dicts import news_dict
from news.models import Article


class GrabberTestCase(TestCase):
    def setUp(self):
        self.grabber = NewsGrabber(**news_dict)

    def test_grabber_successfully_creates_articles(self):
        self.grabber.process()
        self.assertEqual(Article.objects.exists(), True)
