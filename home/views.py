from django.shortcuts import render
from home.models import Songs

def home(request):
    song = Songs()
    song.name1 = "Kya schene"
    song.name2 = "mauka e vardat"
    song.name3 = "kya bolte"
    song.name4 = "iya bhai"
    params={'name1':song.name1,'name2':song.name2,'name3':song.name3,'name4':song.name4}
    return render(request,'index.html',params)



