from django.conf.urls import url
from store import views
from rest_framework.compat import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = ([
    url(r'^stores/$', views.StoreList.as_view(), name='store-list'),
    url(r'^stores/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view(),),
    url(r'^transporters/$', views.TransporterList.as_view(), name='transporter-list'),
    url(r'^transporters/(?P<pk>[0-9]+)/$', views.TransporterDetail.as_view(), ),

])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
