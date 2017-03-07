from django.conf.urls import url 
from django.views.generic.base import RedirectView
from .views import tweetListAPIView, tweetCreateAPIView
urlpatterns = [
    url(r'^$', tweetListAPIView.as_view(), name='list'), # /tweet/
    url(r'^create/$', tweetCreateAPIView.as_view(), name='create')
    
]
