from rest_framework import serializers
from .models import Party


class PartySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Party
        fields = [
            'id', 'owner', 'created_at', 'title',
            'description', 'location', 'is_owner'
        ]
