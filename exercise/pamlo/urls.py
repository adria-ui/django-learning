from django.urls import path
from . import views

urlpatterns = [
   path('myfirstpage',views.myfirstpage,name='myfirstpage'),
   path('mysecondpage',views.mysecondpage,name='mysecondpage'),
   path('mythirdpage',views.mythirdpage,name='mythirdpage')
]