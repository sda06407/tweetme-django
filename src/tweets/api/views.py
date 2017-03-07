from rest_framework import generics
from django.db.models import Q
from .serializers import tweetSerializers
from tweets.models import tweet
from rest_framework import permissions
#from .pagination import StandardResultsPagination


class tweetCreateAPIView(generics.CreateAPIView):
    serializer_class = tweetSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class tweetListAPIView(generics.ListAPIView):
    serializer_class = tweetSerializers
    #pagination_class = StandardResultsPagination
    
    def get_queryset(self, *args, **kwargs):
        qs = tweet.objects.all().order_by('-timestamp')
        query = self.request.GET.get('q', None)
        
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs