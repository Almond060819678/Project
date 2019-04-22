import requests
from lxml import html

from news.helpers.base import BaseGrabber


class NewsGrabber(BaseGrabber):
    def __init__(self, url, xpath, model, proxies=None):
        super().__init__(url, xpath, model)
        self.proxies = proxies

    def get_tree_from_response(self):
        response = requests.get(self.url, proxies=self.proxies)
        return html.fromstring(response.text)
