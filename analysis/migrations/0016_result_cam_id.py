# Generated by Django 3.0.3 on 2020-03-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0015_remove_result_cam_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Cam_ID',
            field=models.CharField(default='asd', max_length=4),
        ),
    ]
