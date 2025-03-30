import logging

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer, LoginSerializer

# Sign-Up View
class SignUpView(APIView):
    def post(self, request):
        print("sccusess")
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Account created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
@api_view(['POST'])
def login(request):
    logging.debug("sccusess")
    return Response({'message': 'Login successfully!'}, status=status.HTTP_200_OK)

