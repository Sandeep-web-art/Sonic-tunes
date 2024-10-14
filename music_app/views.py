from django.shortcuts import render
# Create your views here.
from .models import Song
def song_list(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    return render(request,'apple.html',context)

def music_director_songs(request,Musical_genres):
    songs1 = Song.objects.filter(Musical_genres=Musical_genres)
    return render(request,'music_director_songs.html',{'songs1':songs1})


#To get reload symbol

# import asyncio
# from django.shortcuts import render
# from .models import Song

# async def song_list(request):
#     songs = await Song.objects.all().async()
#     context = {
#         'songs': songs
#     }
#     return render(request, 'apple.html', context)

# async def music_director_songs(request, music_director):
#     songs1 = await Song.objects.filter(music_director=music_director).async()
#     return render(request, 'music_director_songs.html', {'songs1': songs1})