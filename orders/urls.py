from django.conf.urls import url
from orders import views
from rest_framework.compat import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = ([
    url(r'^orders/$', views.OrdersList.as_view(), name='orders-list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrdersDetail.as_view(),),
    url(r'^orders_store/$', views.OrdersStoreList.as_view(), name='ordersstore-list'),
    url(r'^orders_store/(?P<pk>[0-9]+)/$', views.OrdersStoreDetail.as_view(),),
    url(r'^order_items/$', views.OrdersItemList.as_view(), name='orderitems-list'),
    url(r'^order_items/(?P<pk>[0-9]+)/$', views.OrdersItemDetail.as_view()),

])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
