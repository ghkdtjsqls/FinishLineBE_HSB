# serializers.py
from rest_framework import serializers
from .models import MySubjectList

class MySubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySubjectList
        fields = ['year', 'semester', 'sub_area', 'sub_sub', 'sub_name', 'credit', 'grade']