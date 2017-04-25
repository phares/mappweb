from django.conf.urls import url
from address import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # url(r'^products/$', views.drink_list),
    # url(r'^products/(?P<pk>[0-9]+)/$', views.drink_detail),

    url(r'^address/$', views.AdressList.as_view()),
    url(r'^address/(?P<pk>[0-9]+)/$', views.AdressDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)