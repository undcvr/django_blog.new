# Generated by Django 4.2.3 on 2023-07-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
