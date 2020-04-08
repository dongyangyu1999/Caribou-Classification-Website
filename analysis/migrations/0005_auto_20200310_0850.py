# Generated by Django 3.0.3 on 2020-03-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_auto_20200310_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Ruminating_Foraging',
            field=models.CharField(choices=[('Chewing', 'CHEWING'), ('Drinking', 'DRINKING'), ('Eating', 'EATING'), ('Licking', 'LICKING soil for minerals but did not eat'), ('None', 'None of the above'), ('Ruminating', 'RUMINATING')], default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='result',
            name='Video_Quality',
            field=models.CharField(choices=[('Excellent', 'EXCELLENT'), ('Good_to_Fair', 'GOOD to FAIR'), ('Poor', 'POOR'), ('Extremely_Obstructed', 'EXTREMELY OBSTRUCTED')], default='', max_length=20, verbose_name='视频质量'),
        ),
    ]
