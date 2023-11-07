from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = '__all__'

       def create(self, clean_data):
           user_obj = User.objects.create_user(password=clean_data['password'], username=clean_data['username'])
           user_obj.email=clean_data['email']
           user_obj.first_name=clean_data['first_name']
           user_obj.last_name=clean_data['last_name']
           user_obj.gender=clean_data['gender']
           user_obj.phone=clean_data['phone']
           user_obj.save()

           return user_obj.serialize()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, clean_data):
        user = authenticate(username=clean_data['email'], password=clean_data['password'])

        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        return user.serialize()
    

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'gender']
