from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

class UserDetailView(DetailView):
  queryset = User.objects.all()
  template_name = 'accounts/user_detail.html'
  
  
  