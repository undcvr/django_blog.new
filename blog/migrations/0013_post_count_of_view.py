# Generated by Django 4.2.3 on 2023-07-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_of_view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
