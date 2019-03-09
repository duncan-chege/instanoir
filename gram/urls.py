from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home, name = 'home'),
    url(r'^signup/$', views.signup, name = 'signup')
]