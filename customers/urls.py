from django.conf.urls import url, include
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = ([

    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^customers/$', views.UserList.as_view(), name='user-list'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
])

# urlpatterns = format_suffix_patterns(urlpatterns)
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]