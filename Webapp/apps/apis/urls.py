
from django.urls import path
from . import views

urlpatterns = [
   path('test/', views.ApiTest.as_view(), name='ApiTest'),
   path('person-serialize-data/', views.PersonSerializerAPIView.as_view(), name='person-serialize-data'),
   path('person-data-save/', views.PersonAPIView.as_view(), name='person-data-save'),
    
]
