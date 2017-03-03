from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^/create/(?P<id>\d+)$', views.create_secret, name='create_secret'),
    url(r'^/delete/(?P<id>\d+)$', views.delete_secret, name='delete_secret'),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^/like/(?P<user_id>\d+)/(?P<message_id>\d+)$', views.create_like, name='create_like'),
    # url(r'^products/show/(?P<id>\d+)$', views.show, name="show"),
    # url(r'^products/new$', views.new,
]