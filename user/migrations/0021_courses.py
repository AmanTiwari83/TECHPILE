# Generated by Django 3.2.4 on 2023-10-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_placements_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='static/courses/')),
                ('cname', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]