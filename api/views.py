from django.shortcuts import render

# Create your views here.
# jan 2
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializers,TodoSerializer
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions

class RegistrationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class TodosView(ViewSet):# jan 3
    def create(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            authentication_classes=[authentication.BasicAuthentication]
            permission_classes=[permissions.IsAuthenticated]
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
