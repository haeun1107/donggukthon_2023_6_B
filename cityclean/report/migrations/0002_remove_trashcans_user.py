# Generated by Django 5.0 on 2023-12-18 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trashcans',
            name='user',
        ),
    ]
