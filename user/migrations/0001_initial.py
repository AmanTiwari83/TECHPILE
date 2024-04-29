# Generated by Django 3.2.4 on 2023-10-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('apply', models.CharField(max_length=100, null=True)),
                ('college', models.TextField(null=True)),
                ('course', models.TextField(null=True)),
                ('year', models.TextField(null=True)),
                ('contact', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
    ]