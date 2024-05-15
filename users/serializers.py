from users.models import UserAccount
from djoser.serializers import UserSerializer as DjoserUserSerializer
from rest_framework import serializers


class UserSerializer(DjoserUserSerializer):
    # Add your custom fields or override existing ones here
    status = serializers.CharField(default='success')
    message = serializers.CharField(default='User created successfully')

    class Meta(DjoserUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'status', 'message']
        ref_name = 'DjoserUserSerializer'

    def to_representation(self, instance):
        # Get the original serialized data
        data = super().to_representation(instance)

        # Add your custom status and message fields alongside the existing data
        data['status'] = 'success'
        data['message'] = 'User created successfully'

        return data

