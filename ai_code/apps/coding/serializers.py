from rest_framework import serializers
from .models import Coding, CodingExample


class CodingExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingExample
        fields = "__all__"


class CodingSerializer(serializers.ModelSerializer):
    code_examples = CodingExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Coding
        fields = "__all__"
