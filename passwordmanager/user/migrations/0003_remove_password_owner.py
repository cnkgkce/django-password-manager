# Generated by Django 3.2 on 2022-02-18 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_password_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='owner',
        ),
    ]
