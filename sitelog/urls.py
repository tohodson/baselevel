from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new_log, name='new_log'),
    url(r'^list$', views.log_list, name='log_list'),
]
