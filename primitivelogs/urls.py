from django.conf.urls import patterns, include, url

from .views import PrimitiveLogListView

urlpatterns = patterns('',
    url(r'^list/$', PrimitiveLogListView.as_view(), name="plogslist"),
)

