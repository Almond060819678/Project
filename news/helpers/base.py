from abc import ABC

import requests
from lxml import html


class BaseGrabber(ABC):
    """Class demonstrating abstraction for basic grabber. Follow grabbing steps,
    overriding methods if needed
    """

    def __init__(self, url, xpath, model):
        self.url = url
        self.xpath = xpath
        self.model = model

    def process(self):
        """
        Grabbing steps
        """
        tree = self.get_tree_from_response()
        web_elements = self.web_elements_from_html(tree)
        dicts = self.dicts_from_web_elements(web_elements)
        self.dicts_to_instances(dicts)

    def get_tree_from_response(self):
        response = requests.get(self.url)
        return html.fromstring(response.text)

    def web_elements_from_html(self, tree):
        return tree.xpath(self.xpath)

    def dicts_from_web_elements(self, elements):
        dicts = [
            {"title": element.text_content(), "url": element.xpath('./@href')[0]}
            for element in elements]
        return dicts

    def dicts_to_instances(self, dicts):
        for _dict in dicts:
            self.model.objects.get_or_create(**_dict)
