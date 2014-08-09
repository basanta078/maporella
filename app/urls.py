from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/networks$', views.networks),
    url(r'^api/routes$', views.routes),
]