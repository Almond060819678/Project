from django.test import TestCase
from news.grabber import NewsGrabber
from news.models import Article


class GrabberTestCase(TestCase):
    def setUp(self):
        self.grabber = NewsGrabber()

    def test_grabber_successfully_creates_articles(self):
        self.grabber.grab_articles()
        self.assertEqual(Article.objects.exists(), True)
