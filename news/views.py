from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from news.API.exceptions import InvalidAPIQuery
from news.API.ordering_filter import CustomOrderingFilter
from news.grabber import NewsGrabber
from news.helpers.grabber_dicts import news_dict
from news.models import Article
from news.serializers import ArticleSerializer


@api_view(['GET'])
def api_root(request):
    return Response({
        'articles': reverse('posts-list', request=request),
    })


class PostsList(generics.ListAPIView):
    model = Article
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = (CustomOrderingFilter,)
    ordering_fields = [field.attname for field in Article._meta.fields]

    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except (ValueError, KeyError):
            raise InvalidAPIQuery


def run_news_grabber(request):
    NewsGrabber(**news_dict).process()
    return HttpResponse("Grab articles method was called")


def redirect_view(request):
    response = redirect('posts/')
    return response
