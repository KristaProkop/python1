from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books$', views.index, name="index"),
    url(r'^books/add$', views.create, name='create'),
    url(r'^books/(?P<id>\d+)$', views.show_book, name='show_book'),
    url(r'^books/add/(?P<id>\d+)$', views.create_review, name='create_review'),
    url(r'^users/(?P<id>\d+)$', views.show_user, name='show_user'),

#     url(r'^/$', views.most_popular, name="most_popular"),
#     url(r'^/create/(?P<id>\d+)$', views.create_secret, name='create_secret'),
]