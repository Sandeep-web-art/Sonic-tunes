from django.shortcuts import render
from .models import Song


# Create your views here.
def song_list(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return   render(request, 'main.html',context)

def music_detail(request,music_generes):
    songs = Song.objects.filter(genre= music_generes)
    return render(request,'second.html',{'songs':songs})

