# Generated by Django 3.2.4 on 2023-10-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_videogallery_vlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='placements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='static/placement/')),
                ('name', models.CharField(max_length=200, null=True)),
                ('college', models.TextField(null=True)),
                ('year', models.IntegerField(null=True)),
            ],
        ),
    ]
