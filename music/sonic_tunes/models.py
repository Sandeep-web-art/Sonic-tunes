from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_files =  models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='images/')
    music_generes =  models.CharField(max_length=255)


    def  __str__(self):
        return self.music_generes


