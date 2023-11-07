from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'gender', 'phone', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    #def validate(self, data):
    #    if data['password'] != data['confirmPassword']:
    #        raise serializers.ValidationError("Las contraseñas no coinciden.")
    #    return data