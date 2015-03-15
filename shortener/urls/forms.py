from django.forms import ModelForm

from .models import URL, Collection


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ('url',)


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ('urls',)
