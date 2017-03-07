from django.shortcuts import render
from .models import tweet
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import tweetModelForm
from django.core.urlresolvers import reverse_lazy
#from django.forms.utils import ErrorList
from .mixins import FormUserNeedMixun, UserOwnerMixin
#from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.
class tweetCreateView(FormUserNeedMixun, CreateView):
   # queryset = tweet.objects.all()
    form_class = tweetModelForm
    template_name = 'tweets/create_view.html'
    #success_url = reverse_lazy("tweet:detail")
    #login_url = '/admin/'
    #fields = ['user','content']
    
class tweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = tweet.objects.all()
    template_name = 'tweets/update_view.html'
    form_class = tweetModelForm
    success_url = '/tweet/'

    
class tweetDeleteView(LoginRequiredMixin, DeleteView):
    model = tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list") #tweet/list
    
"""
    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(tweetCreateView, self).form_valid(form)
        else:
            form._error[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged'])
            return self.form_invalid(form)
   
def tweet_create_page(request):
    form = tweetModelForm(request.POST or None)
    if form.is_vaild():
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
    context = {
        'form':form
    }
    return render(request,'tweets/create_view.html',context)
"""         
    

#detail
class tweetDetailView(DetailView):

    queryset = tweet.objects.all()
    template_name = "tweets/detail_view.html"
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return tweet.objects.get(id = pk)

class tweetListView(ListView):
    def get_queryset(self, *args, **kwargs):
        qs = tweet.objects.all()
        query = self.request.GET.get('q', None)
        
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs
    
        
    template_name = "tweets/list_view.html"
    def get_context_data(self, *args, **kwargs):
        context = super(tweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = tweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
       # context["another_context"] = tweet.objects.all()
        return context
    

"""

def tweet_detail_view(request,id=7):
    
    obj = tweet.objects.get(id=id)#get from database
    print(obj)
    context = {
        "object" : obj
    }
    
    return render(request,"tweets/detail_view.html",context)
"""
"""
def tweet_list_view(request):
    
    queryset = tweet.objects.all()
    print(queryset)
    context = {
        "object_list" : queryset
    }
    
    return render(request,"tweets/list_view.html",context)

"""