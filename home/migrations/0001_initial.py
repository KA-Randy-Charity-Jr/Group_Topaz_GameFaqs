# Generated by Django 3.1.2 on 2020-10-08 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('date_realesed', models.DateField()),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Gamefaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=280)),
                ('game', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='home.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gamefaqs',
            field=models.ManyToManyField(blank=True, related_name='faqs', to='home.Gamefaq'),
        ),
    ]
