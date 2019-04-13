from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from news.models import Article
from news.serializers import ArticleSerializer
from news.grabber import NewsGrabber
from django.http import HttpResponse
from news.customizing_api.exceptions import InvalidAPIQuery
from django.shortcuts import redirect
from news.customizing_api.ordering_filter import CustomOrderingFilter


@api_view(['GET'])
def api_root(request):
    return Response({
        'articles': reverse('article-list', request=request),
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


def run_grabber(request):
    NewsGrabber().grab_articles()
    return HttpResponse("Grab articles method was called")


def redirect_view(request):
    response = redirect('posts/')
    return response
