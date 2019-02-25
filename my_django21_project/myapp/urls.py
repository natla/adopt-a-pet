from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = "myapp"
urlpatterns = [
    url(r'^(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    url(r'^$', views.post_list_view, name='post_list_view'),
]
