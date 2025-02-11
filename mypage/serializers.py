from rest_framework import serializers
from .models import User, MyPage

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','nickname','profile']