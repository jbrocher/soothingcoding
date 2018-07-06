from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^', views.new_potential, name='new_potential'),
]
