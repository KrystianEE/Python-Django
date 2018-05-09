from django.conf.urls import url
from board_page import views

urlpatterns = [
    url('^$', views.board, name='board_page'),
]
