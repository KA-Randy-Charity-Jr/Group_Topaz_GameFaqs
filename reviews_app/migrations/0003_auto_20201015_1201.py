# Generated by Django 3.1.2 on 2020-10-15 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0002_auto_20201015_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='upvotes',
        ),
    ]
