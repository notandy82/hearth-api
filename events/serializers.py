# from rest_framework import serializers
# from events.models import Event


# class EventSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     is_owner = serializers.SerializerMethodField()
#     date = serializers.DateField(input_formats=['%m/%d/%Y'])

#     def get_is_owner(self, obj):
#         request = self.context['request']
#         return request.user == obj.owner

#     class Meta:
#         model = Event
#         fields = [
#             'id', 'owner', 'date', 'title', 'is_owner'
#         ]
