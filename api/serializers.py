from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
      
  
    
class userserializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'


    def create(self, validated_data):
        return  User.objects.create_user(**validated_data)
    

    def update(self, instance, validated_data):

        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.password)
        instance.save()
        return instance

        


class UserRegisterSerializer(serializers.ModelSerializer):
    re_password=serializers.CharField(write_only=True,required=True)

    class Meta:
        model=User
        fields=['username','email','password','re_password']

    
    def create(self, validated_data):
        del validated_data['re_password']
        return  User.objects.create_user(**validated_data)
        

