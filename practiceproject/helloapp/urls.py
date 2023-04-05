from django.urls import path
from . import views   # all views.py method is acceesible here
urlpatterns = [
path('',views.index,name='index')
]