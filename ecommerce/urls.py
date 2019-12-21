from django.conf.urls import url
from .views import home

app_name ='ecommerce'

urlpatterns = [
    url('',home, name='home')
]