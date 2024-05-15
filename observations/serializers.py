# serializers.py
from rest_framework import serializers
from .models import Observation
from .models import ApiKeys
import uuid


def generate_api_key():
    """
    Generate a random API key.
    """
    return str(uuid.uuid4())


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'


class APIKeySerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(read_only=True)

    class Meta:
        model = ApiKeys
        fields = ['user_id', 'api_key', 'expires_at']

    def create(self, validated_data):
        user_id = validated_data.get('user_id')

        # Check if an API key already exists for the user
        existing_api_key = ApiKeys.objects.filter(user_id=user_id).first()
        if existing_api_key:
            # Update the existing API key with a new one
            existing_api_key.api_key = generate_api_key()
            existing_api_key.save()
            return existing_api_key

        # Generate a new API key if one doesn't exist
        validated_data['api_key'] = generate_api_key()
        return super().create(validated_data)