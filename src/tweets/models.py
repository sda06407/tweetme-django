from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_content
from django.core.urlresolvers import reverse
# Create your models here.
"""
def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError("Content cannot be abc")
    return value
"""
#model manager

class tweet(models.Model):
    #user
    user      = models.ForeignKey(settings.AUTH_USER_MODEL)
    content   = models.CharField(max_length=140, validators = [validate_content])
    updated   = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})
        
#    class Meta:
#        ordering = ['-timestamp', 'content']
""" 
    def clean(self, *args, **kwargs):
        content = self.content
        if content == "abc":
            raise ValidationError("Cann nor be ABC")
        return super(tweet, self).clean(*args, **kwargs)
"""