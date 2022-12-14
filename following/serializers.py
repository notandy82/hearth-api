from rest_framework import serializers
from .models import Following
from django.db import IntegrityError


class FollowingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.title')

    class Meta:
        model = Following
        fields = [
            'id', 'owner', 'created_at',
            'followed', 'followed_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
