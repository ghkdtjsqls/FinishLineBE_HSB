# user_auth/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'department', 'studentId', 'majortype', 'secondmajor', 'microdegree', 'password']

    def create(self, validated_data):
        # 비밀번호 해시화
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
