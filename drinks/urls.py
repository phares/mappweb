from django.conf.urls import url
from drinks import views

urlpatterns = [
    url(r'^drinks/$', views.drink_list),
    url(r'^drinks/(?P<pk>[0-9]+)/$', views.drink_detail),
]