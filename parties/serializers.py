from rest_framework import serializers
from .models import Party
from profiles.models import Profile
from following.models import Following


class PartySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    party_image = serializers.ReadOnlyField(source='party.image.url')
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 4 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 4MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Following.objects.filter(
                owner=user, followed=obj.id
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Party
        fields = [
            'id', 'owner', 'created_at', 'image', 'party_image',
            'title', 'description', 'location', 'is_owner',
            'following_id', 'posts_count'
        ]
