from django.db import models


class Article(models.Model):
    title = models.TextField()
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
