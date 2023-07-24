# Generated by Django 4.2.3 on 2023-07-24 03:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0021_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_check',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
