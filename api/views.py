from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .serializers import Taskserializer, userserializer,UserRegisterSerializer
from tasks.models import Task
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly





class userapiviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    def get_serializer_class(self):
        match self.action:

            case 'list':
                return userserializer
            case 'create':
                return userserializer
            case 'update':
                return UserRegisterSerializer
            case 'retrive':
                return userserializer
            case 'partial_update':
                return userserializer
            case 'destroy':
                return userserializer



class taskviewset(viewsets.ModelViewSet):
    serializer_class = Taskserializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]


    def get_queryset(self):
        if self.action == 'list':
            return self.request.user.tasks.all()
        else:
            return Task.objects.all()
          
            
    
    


        

    

