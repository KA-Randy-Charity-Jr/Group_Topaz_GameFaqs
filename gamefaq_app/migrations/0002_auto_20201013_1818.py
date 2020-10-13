# Generated by Django 3.1.2 on 2020-10-13 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
        ('gamefaq_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamefaq',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_game', to='game_app.game'),
        ),
    ]