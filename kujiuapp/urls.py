# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views

# 通过app_name告诉Django这个urls.py模块是属于 kujiuapp 应用的，这种技术叫做视图函数命名空间。
app_name = 'kujiuapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]