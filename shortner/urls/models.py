from django.db import models
import shortuuid


class URL(models.Model):

    url = models.URLField(blank=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=255, blank=False, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.hash = self.get_hash(self.url)
        super(URL, self).save(force_insert, force_update, using, update_fields)

    @staticmethod
    def get_hash(string):
        return shortuuid.uuid(name=string.encode(encoding='utf-8'))[0:5]


class Collection(models.Model):

    urls = models.ManyToManyField('URL')
    created_at = models.DateTimeField(auto_now_add=True)
