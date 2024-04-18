#use of serializers are  described in mobileapp

from rest_framework import serializers
from django.contrib.auth.models import User
from todoapp.models import Todos

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

    def create(self,validated_data):# overriding create method in serializers jan2
        return User.objects.create_user(**validated_data)# ** is unpacking
        
class TodoSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()#jan 3
    class Meta:
        model=Todos
        fields='__all__'
        read_only_fields=['id','status','user']