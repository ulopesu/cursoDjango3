# Generated by Django 3.0.6 on 2020-05-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='deleted',
        ),
        migrations.AddField(
            model_name='post',
            name='activated',
            field=models.BooleanField(default=True),
        ),
    ]
