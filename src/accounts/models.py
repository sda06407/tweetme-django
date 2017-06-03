from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class UserProfileManager(models.Manager):
  def all(self):
    qs = self.get_queryset().all()
    #print(dir(self))
    return  qs
#  def toggle_follow(self, user, to_toggle_user):
#   user_profile, create = 

objects = UserProfileManager() #UserProfile.objects.all()
class UserProfile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile") #user.profile
  following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') #user.profile.followed_by
  
  def __str__(self):
    return str(self.following.all().count())