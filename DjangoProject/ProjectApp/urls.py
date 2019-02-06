from django.conf.urls import url
from ProjectApp import views

urlpatterns = [
    url(r'^$',views.users,name='users')
]
