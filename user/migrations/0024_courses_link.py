# Generated by Django 3.2.4 on 2023-10-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20231005_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
