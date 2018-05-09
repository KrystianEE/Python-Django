from django.conf.urls import url
from appone import views

urlpatterns = [
    url('^$', views.help, name='help'),
]
