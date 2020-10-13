# Generated by Django 3.1.2 on 2020-10-12 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamefaq_app', '0005_auto_20201010_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Body', models.TextField()),
                ('isreccomend', models.BooleanField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL)),
                ('gamefaq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewgamefaq', to='gamefaq_app.gamefaq')),
            ],
        ),
    ]
