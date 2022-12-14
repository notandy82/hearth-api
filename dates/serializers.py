from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Event
        fields = (
            'id', 'owner', 'party',
            'title', 'about', 'when', 'is_owner'
        )
