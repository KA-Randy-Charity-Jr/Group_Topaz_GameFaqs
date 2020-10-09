# Generated by Django 3.1.2 on 2020-10-09 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0002_remove_game_gamefaq'),
        ('gamefaq_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamefaq',
            name='faq_game',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_game', to='game_app.game'),
        ),
    ]
