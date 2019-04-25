from abc import ABC
from contextlib import closing

import requests
from lxml import html


class BaseGrabber(ABC):
    """Class demonstrating abstraction for basic grabber.
    instruction for configuring your personal grabber:
    1. Inherit from this base class.
    2. When initiating your subclass instance, give it the following arguments:
    - url
    - xpath
    - model
    - proxies (optional)
    3. Process method consists of 4 methods (parts). Complete or override them if required:
    - get_html_tree_from_response
    - web_elements_from_html
    - dicts_from_web_elements
    - dicts_to_instances
    """

    def __init__(self, url, xpath, model):
        self.url = url
        self.xpath = xpath
        self.model = model
        self.proxies = None

    def process(self):
        """
        Grabbing steps
        """
        tree = self.get_html_tree_from_response()
        if tree is not None:
            web_elements = self.web_elements_from_html(tree)
            dicts = self.dicts_from_web_elements(web_elements)
            self.dicts_to_instances(dicts)

    def get_html_tree_from_response(self):
        try:
            with closing(requests.get(self.url, stream=True, proxies=self.proxies)) as response:
                if not self.is_good_response(response):
                    return None
                return html.fromstring(response.text)
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def is_good_response(response):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = response.headers['Content-Type'].lower()
        return (response.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def web_elements_from_html(self, tree):
        return tree.xpath(self.xpath)

    @staticmethod
    def dicts_from_web_elements(elements):
        """
        Define here your models fields as keys and how to get values from web elements for given xpath
        """
        dicts = [{} for element in elements]
        return dicts

    def dicts_to_instances(self, dicts):
        for _dict in dicts:
            self.model.objects.get_or_create(**_dict)
