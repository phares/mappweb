from django.conf.urls import url
from address import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # url(r'^products/$', views.drink_list),
    # url(r'^products/(?P<pk>[0-9]+)/$', views.drink_detail),

    url(r'^address/$', views.AddressList.as_view(), name='address-list'),
    url(r'^address/(?P<pk>[0-9]+)/$', views.AddressDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)