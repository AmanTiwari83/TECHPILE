# Generated by Django 3.2.4 on 2023-10-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20231005_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='cname',
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='image',
            field=models.ImageField(null=True, upload_to='static/courses'),
        ),
        migrations.AddField(
            model_name='courses',
            name='coursecategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.coursecategory'),
        ),
    ]
