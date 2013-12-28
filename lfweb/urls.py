from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('lfweb.views',
    url(r'^(?P<slug>\w+)', "detail",name = "detail"),
    url(r'^', "collections",name = "collections"),
)
