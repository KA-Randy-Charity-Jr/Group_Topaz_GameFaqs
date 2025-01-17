# Generated by Django 3.1.2 on 2020-10-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('console_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.TextField(choices=[('ACTION', 'ACTION'), ('RPG', 'RPG'), ('SHOOTER', 'SHOOTER'), ('HORROR', 'HORROR')], max_length=40)),
                ('date_realesed', models.DateField()),
                ('image', models.ImageField(upload_to='gallery')),
                ('consoles', models.ManyToManyField(blank=True, related_name='console_game', to='console_app.Console')),
            ],
        ),
    ]
