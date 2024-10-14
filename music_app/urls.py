from django.urls import path
from . import views 

urlpatterns = [
     path('', views.song_list),  
     path('Musical_genres/<str:Musical_genres>/', views.music_director_songs, name="Musical_genres"),
]                                                                            