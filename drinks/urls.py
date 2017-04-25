from django.conf.urls import url
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^drinks/$', views.drink_list),
    url(r'^drinks/(?P<pk>[0-9]+)/$', views.drink_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)