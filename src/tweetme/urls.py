# urls in tweetme
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from tweets.views import tweetListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tweetListView.as_view(), name='home'),
    url(r'^tweet/', include('tweets.urls', namespace = "tweet")),
    url(r'^', include('accounts.urls', namespace = "profile")),
    url(r'^api/tweet/', include('tweets.api.urls', namespace = "tweet-api") )
]
if settings.DEBUG:
   urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))