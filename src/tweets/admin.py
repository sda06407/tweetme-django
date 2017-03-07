from django.contrib import admin

from .forms import tweetModelForm
# Register your models here.
from .models import tweet


class tweetModelAdmin(admin.ModelAdmin):
    #form = tweetModelForm
    class Meta:
       model = tweet

admin.site.register(tweet, tweetModelAdmin)