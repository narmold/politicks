from django.conf.urls import url

from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uri>[0-9]+)/$', views.detail, name='detail'),
] + staticfiles_urlpatterns()
