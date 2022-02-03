from django.shortcuts import render
from home.models import Songs

def home(request):
    song = Songs.objects.all()
    
    
    return render(request,'index.html',{'song':song})



