# Generated by Django 5.0.4 on 2024-04-21 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_task_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
