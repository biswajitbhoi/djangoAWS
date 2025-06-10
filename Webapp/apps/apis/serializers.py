from rest_framework import serializers
from .models import Person

class PersonTestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(min_value=0)
    city = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Name cannot contain numbers.")
        return value


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Name cannot contain numbers.")
        return value