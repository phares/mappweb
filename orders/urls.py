from django.conf.urls import url
from orders import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # url(r'^products/$', views.drink_list),
    # url(r'^products/(?P<pk>[0-9]+)/$', views.drink_detail),

    url(r'^orders/$', views.OrdersList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrdersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)