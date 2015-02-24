from django.db import models


class URL(models.Model):

    url = models.URLField(blank=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Collection(models.Model):

    urls = models.ManyToManyField('URL')
    created_at = models.DateTimeField(auto_now_add=True)
