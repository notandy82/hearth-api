from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = (
            'id', 'owner', 'party',
            'title', 'about', 'when'
        )
