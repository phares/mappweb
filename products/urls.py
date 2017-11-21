from django.conf.urls import url, include
from products import views
from rest_framework.urlpatterns import format_suffix_patterns

# API endpoints
urlpatterns = ([

    # url(r'^products/$', views.drink_list),
    # url(r'^products/(?P<pk>[0-9]+)/$', views.drink_detail),


    url(r'^$', views.api_root),
    url(r'^products/$', views.ProductList.as_view(), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product-detail'),
    # url(r'^products/$', views.ProductList.as_view()),
    # url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^categories/$', views.ProductCategoryList.as_view(), name='productcategory-list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.ProductCategoryDetail.as_view(), name='productcategory-detail'),

    url(r'^display/$', views.DisplayList.as_view(), name='display-list'),
    url(r'^display/(?P<pk>[0-9]+)/$', views.DisplayDetail.as_view(), name='display-detail'),
])

# urlpatterns = format_suffix_patterns(urlpatterns)

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]