# Generated by Django 3.1.2 on 2020-10-14 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console_app', '0001_initial'),
        ('gamefaq_app', '0003_auto_20201014_0722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamefaq',
            name='consoles',
        ),
        migrations.AddField(
            model_name='gamefaq',
            name='consoles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='console_gamefaq', to='console_app.console'),
        ),
    ]
