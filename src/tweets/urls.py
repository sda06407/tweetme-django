"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# urls in tweets
from .views import  tweetDetailView ,tweetListView, tweetCreateView, tweetUpdateView, tweetDetailView, tweetDeleteView
from django.conf.urls import url 
from django.views.generic.base import RedirectView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', tweetListView.as_view(), name='list'), # /tweet/
    url(r'^(?P<pk>\d+)/$', tweetDetailView.as_view(), name="detail"), #/tweet/1
    url(r'^create/$', tweetCreateView.as_view(), name='create'), #/tweet/create
    url(r'^(?P<pk>\d+)/update$', tweetUpdateView.as_view(), name='update'),#/tweet/1/update
    url(r'^(?P<pk>\d+)/delete$', tweetDeleteView.as_view(), name='delete')#/tweet/1/delete
]
