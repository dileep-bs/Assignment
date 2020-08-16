from rest_framework import serializers
from .models import Profile

class CsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name','email','address','phone','profile']

