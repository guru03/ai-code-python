
from rest_framework import serializers
from .models import Angular


class AngularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angular
        fields = "__all__"