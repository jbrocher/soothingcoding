from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.contact_form, name='contact_form'),
    url(r'^/new_potential/$', views.new_potential, name='new_potential'),
]
