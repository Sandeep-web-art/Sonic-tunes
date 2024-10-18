from django.urls import path
from . import views


urlpatterns =[
    path('', views.song_list),
    path('genres/<str:Music_generes>/', views.music_detail, name="music_generes"),


]