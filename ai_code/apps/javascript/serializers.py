
from rest_framework import serializers
from .models import Javascript


class JavascriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javascript
        fields = "__all__"