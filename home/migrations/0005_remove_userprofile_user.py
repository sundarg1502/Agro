# Generated by Django 5.1.2 on 2024-12-18 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]