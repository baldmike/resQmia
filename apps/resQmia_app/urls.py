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

    url(r'^new_cat$', views.new_cat),
    url(r'^rescue_cat$', views.rescue_cat),
    
    url(r'^select_dashboard/(?P<dog_id>\d+)$', views.select_dashboard),
    url(r'^select_our_cats/(?P<cat_id>\d+)$', views.select_our_cats),
    url(r'^select_dashboard/(?P<dog_id>\d+)$', views.select_dashboard),
    url(r'^select_dashboard_cat/(?P<cat_id>\d+)$', views.select_dashboard_cat),

    url(r'^our_dogs$', views.our_dogs),
    url(r'^our_cats$', views.our_cats),
    
    url(r'^select_day/(?P<dog_id>\d+)$', views.select_day),

    url(r'^new_vaccine_dog/(?P<id>\d+)$', views.new_vaccine_dog),
    url(r'^new_prevention_dog/(?P<id>\d+)$', views.new_prevention_dog),
    url(r'^new_test_dog/(?P<id>\d+)$', views.new_test_dog),
    url(r'^new_vaccine_cat/(?P<id>\d+)$', views.new_vaccine_cat),
    url(r'^new_prevention_cat/(?P<id>\d+)$', views.new_prevention_cat),
    url(r'^new_test_cat/(?P<id>\d+)$', views.new_test_cat),

    url(r'^select_adopted/(?P<dog_id>\d+)$', views.select_adopted),
    url(r'^adopted/(?P<dog_id>\d+)$', views.adopted),
    
    url(r'^adopted_dogs$', views.adopted_dogs),


    url(r'^delete_dog/(?P<dog_id>\d+)$', views.delete_dog),
    url(r'^delete_cat/(?P<cat_id>\d+)$', views.delete_cat),

]