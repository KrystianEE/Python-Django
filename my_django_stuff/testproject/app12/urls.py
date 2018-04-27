from django.conf.urls import url
from app12 import views

urlpatterns = [
    url('', views.index, name='index')
]
