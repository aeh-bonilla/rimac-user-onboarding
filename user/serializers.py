from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    genres = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = User
        fields = '__all__'
