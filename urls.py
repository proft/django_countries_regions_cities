from django.conf.urls import *
from .views import *

urlpatterns = patterns(
    '',
    url(r'^$', TestModelView.as_view(), name="testmodel"),
)
