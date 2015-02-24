from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
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
