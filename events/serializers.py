from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer
    """
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id', 'owner', 'title',
            'description', 'when', 'location'
        )
