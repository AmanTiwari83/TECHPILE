# Generated by Django 3.2.4 on 2023-10-02 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='date',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='enroll',
        ),
    ]