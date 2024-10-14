# Generated by Django 5.1.2 on 2024-10-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('image', models.ImageField(upload_to='images/')),
                ('Musical_genres', models.CharField(max_length=100)),
            ],
        ),
    ]
