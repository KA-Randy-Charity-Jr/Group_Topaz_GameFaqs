# Generated by Django 3.1.2 on 2020-10-10 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0002_remove_game_gamefaq'),
        ('gamefaq_app', '0004_auto_20201010_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamefaq',
            name='game',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_game', to='game_app.game'),
        ),
    ]
