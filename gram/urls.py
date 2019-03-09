from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.landing, name = 'landing'),
    url(r'^signup/$', views.signup, name = 'signup')
]