from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from users.serializers import RegisterSerializer

# Create your views here.



class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self , request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({
                "User" : serializer.data , 
                "Message":"註冊成功",
                
            },status = status.HTTP_201_CREATED)

        return Response({'Error':'發生錯誤'} , status=status.HTTP_400_BAD_REQUEST)
