from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .forms import TestModelForm


class TestModelView(CreateView):
    form_class = TestModelForm
    template_name = 'countries_regions_cities/index.html'

    def get_success_url(self):
        return reverse('testmodel')
