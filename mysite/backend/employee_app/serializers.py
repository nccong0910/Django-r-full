from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields = "__all__"