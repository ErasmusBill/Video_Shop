# Generated by Django 5.0.1 on 2024-07-03 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_alter_authorities_options_video_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
