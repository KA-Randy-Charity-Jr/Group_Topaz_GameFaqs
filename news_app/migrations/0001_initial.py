# Generated by Django 3.1.2 on 2020-10-09 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='news_author', to=settings.AUTH_USER_MODEL)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thegame', to='game_app.game')),
            ],
        ),
    ]
