# Generated by Django 3.0.3 on 2020-04-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0018_auto_20200323_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Does_the_cow_have_antlers',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('cant see', "Can't see/Not sure/Not relevant")], max_length=20),
        ),
        migrations.AlterField(
            model_name='result',
            name='Other_caribou_visible_excluding_own_calf',
            field=models.CharField(choices=[('Yes_one_to_a_few', 'Yes – one to a few individuals'), ('Yes_herd', 'Yes – herd'), ('Yes', 'Yes'), ('No', 'No')], max_length=20),
        ),
    ]