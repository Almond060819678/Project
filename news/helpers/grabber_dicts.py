from news.models import Article

news_dict = {
    'url': 'https://news.ycombinator.com/',
    'xpath': '//table[@id="hnmain"]//table[@class="itemlist"]//tr[@class="athing"]/td[@class="title"]/a',
    'model': Article
}
