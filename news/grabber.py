import requests
from lxml import html
from news.models import Article

articles_xpath = '//table[@id="hnmain"]//table[@class="itemlist"]//tr[@class="athing"]/td[@class="title"]/a'


class NewsGrabber:
    url = 'https://news.ycombinator.com/'
    proxies = {
        'http': 'http://68.183.42.79:3128',
        'https': 'http://68.183.42.79:3128'
    }

    def grab_articles(self):
        response = requests.get(self.url, proxies=self.proxies)
        tree = html.fromstring(response.text)
        article_elements = tree.xpath(articles_xpath)
        article_dicts = [
            {"title": element.text_content(), "url": element.xpath('./@href')[0]}
            for element in article_elements
        ]
        for article in article_dicts:
            Article.objects.get_or_create(**article)
