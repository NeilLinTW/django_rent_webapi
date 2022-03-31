from datetime import *
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from adv.serializers import AdvSerializer, RateSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Advertisement
# Create your views here.

class AdvList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AdvSerializer

    def perform_create(self,serializer):
        user = self.request.user
        userid = str(user.id)
        print('*****************');
        print(userid);

        serializer.save(User_id = userid)

class AdvSearch(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AdvSerializer

    def get_queryset(self):
        queryset = Advertisement.objects.filter(IsEnable = True).filter(City = self.kwargs['city']).filter(Town = self.kwargs['town']);

        return queryset;


class AdvDetail(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AdvSerializer

    def get_queryset(self):
        queryset = Advertisement.objects.filter(IsEnable = True).filter(Id = self.kwargs['id']);

        return queryset;


class UpdateAdv(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AdvSerializer
    queryset = Advertisement.objects.all()

    def perform_update(self,serializer):
        user = self.request.user
        userid = str(user.id)
        # adv = Advertisement.objects.filter(Id = self.kwargs['pk'])
        # adv.ModifyDate = datetime.now()
        serializer.save(ModifyDate = datetime.now())

        # queryset = Advertisement.objects.filter(id = self.kwargs['pk'])
   

class RateCreate(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RateSerializer

    def perform_create(self,serializer):
        serializer.save()