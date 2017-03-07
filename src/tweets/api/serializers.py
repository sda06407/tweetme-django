from django.utils.timesince import timesince
from rest_framework import serializers
from tweets.models import tweet
from accounts.api.serializers import UserDisplaySerializer
class tweetSerializers(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only = True) #write only
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]
        
    def get_date_display(self, obj):
        return obj.timestamp.strftime("%d %b %Y : %M %p")
        
    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"