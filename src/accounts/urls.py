from .views import  UserDetailView
from django.conf.urls import url 
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name="profile")
]