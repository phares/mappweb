from django.conf.urls import url, include
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.forms import UserCreationForm

urlpatterns = ([

    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^customers/$', views.UserList.as_view(), name='user-list'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^customers/feedback/$', views.FeedbackList.as_view(), name='feedback-list'),
    url(r'^customers/feedback/(?P<pk>[0-9]+)/$', views.FeedbackDetail.as_view(), name='feedback-detail')
])

# urlpatterns = format_suffix_patterns(urlpatterns)
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]