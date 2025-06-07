
from django.urls import path
from . import views

urlpatterns = [
   path('test/', views.ApiTest.as_view(), name='ApiTest'),
    
]
