from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from .models import URL, Collection
from .forms import URLForm


class HomeView(TemplateView):
    template_name = 'shortner/base.html'
home_view = HomeView.as_view()


class URLListView(ListView):
    model = URL
    template_name = 'url/list.html'
    context_object_name = 'urls'
url_list_view = URLListView.as_view()


class URLCreateView(CreateView):
    model = URL
    form_class = URLForm
    template_name = 'url/create.html'
    success_url = reverse_lazy('list')
url_create_view = URLCreateView.as_view()


class HashRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        shortened_hash = kwargs.pop('hash')
        url = get_object_or_404(URL, hash=shortened_hash)
        return url.original_url
hash_redirect_view = HashRedirectView.as_view()
