from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    date = date = fields.DateField(input_formats=['%A, %d-%B, %Y'])

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'date', 'title', 'is_owner'
        ]