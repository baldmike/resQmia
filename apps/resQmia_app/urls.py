from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^logout$', views.logout, name='logout'),

    url(r'^new_dog$', views.new_dog),
    url(r'^rescue_dog$', views.rescue_dog),
    url(r'^select/(?P<dog_id>\d+)$', views.select),
    url(r'^delete/(?P<dog_id>\d+)$', views.delete),
    url(r'^select_day/(?P<dog_id>\d+)$', views.select_day),
    url(r'^select_adopted/(?P<dog_id>\d+)$', views.select_adopted),
    url(r'^adopted/(?P<dog_id>\d+)$', views.adopted),
    url(r'^our_dogs$', views.our_dogs),
    url(r'^adopted_dogs$', views.adopted_dogs),

]