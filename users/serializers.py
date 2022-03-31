from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50 , min_length=10)
    password = serializers.CharField(max_length=100 , write_only=True)
    username = serializers.CharField(max_length=30 , min_length=6)

    class Meta:
        model = User
        fields = ('username' , 'email' , 'password')

    def validate(self , args):
        email = args.get('email',None)
        username = args.get('username',None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email已存在')})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username已存在')})

        return super().validate(args)


    def  create(self , validate_data):
        return User.objects.createuser(**validate_data)




