from django.conf.urls import url
from products import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # url(r'^products/$', views.drink_list),
    # url(r'^products/(?P<pk>[0-9]+)/$', views.drink_detail),

    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)