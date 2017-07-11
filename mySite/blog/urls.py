from django.conf.urls import url
from . impport views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list');
]
