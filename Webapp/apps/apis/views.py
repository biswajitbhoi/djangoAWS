from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status   


class ApiTest(APIView):
    """
    API View for testing purposes.
    """
    
    def get(self, request):
        """
        Handle GET requests.
        """
        data = {
            'message': 'Hello, this is a test response from the API2!'
        }
        return Response(data)  # You can also use status=status.HTTP_200_OK if needed

# Create your views here.
