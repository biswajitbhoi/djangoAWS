from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer,PersonTestSerializer
from rest_framework import status   

# Create your views here.
class ApiTest(APIView):
    """
    API View for testing purposes.
    """
    
    def get(self, request):
        """
        Handle GET requests.
        """
        data = {
            'status' : status.HTTP_200_OK,
            'message': 'Hello, this is a test response from the API3!'
        }
        return Response(data)  # You can also use status=status.HTTP_200_OK if needed

# serializer Test.

class PersonSerializerAPIView(APIView):
    def post(self, request):
        serializer = PersonTestSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": "Data is valid!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Create your views here.

class PersonAPIView(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Data is valid!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
