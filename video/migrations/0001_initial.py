# Generated by Django 5.0.1 on 2024-06-29 22:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upcoming_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailer_url', models.URLField()),
                ('thumbnails', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
                ('thumbnails', models.ImageField(upload_to='media')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]