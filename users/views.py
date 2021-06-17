#Third party imports
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#Local application imports
from .models import User
from .serializers import UserSerializer



# Create your views here.


class UserList(APIView):
    
    def get(self, request):
        try:
            User_list = User.objects.all()
            serializer = UserSerializer(User_list, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"There's been an error {repr(e)}")
            
    def post(self, request):
        data = request.data.copy()
        try:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(f"Created User {request.data.get('username')}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error creating User {request.data.get('username')}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)