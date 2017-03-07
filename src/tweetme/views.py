from django.shortcuts import render

#GET -- tamplate home.html
def home(request):
    return render(request,"home.html",{})
    
