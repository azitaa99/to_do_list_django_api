# Generated by Django 5.0.5 on 2024-05-13 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complite', '-created'], 'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
    ]
