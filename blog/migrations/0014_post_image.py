# Generated by Django 4.2.3 on 2023-07-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_count_of_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='static/media/post.jpg', upload_to=''),
        ),
    ]
