# Generated by Django 3.2.4 on 2023-10-02 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='apply',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='course',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='year',
        ),
    ]