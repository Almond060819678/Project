from news.helpers.base import BaseGrabber


class NewsGrabber(BaseGrabber):
    def __init__(self, url, xpath, model, proxies=None):
        super().__init__(url, xpath, model)
        self.proxies = proxies

    @staticmethod
    def dicts_from_web_elements(elements):
        dicts = [
            {"title": element.text_content(), "url": element.xpath('./@href')[0]}
            for element in elements]
        return dicts
