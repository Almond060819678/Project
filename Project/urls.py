from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.PostsList.as_view(), name='article-list'),
    path('grab_posts/', views.run_grabber, name='grab-posts'),
    path('', views.redirect_view),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
