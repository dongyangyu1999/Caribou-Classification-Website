# Generated by Django 3.0.3 on 2020-03-23 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0009_auto_20200310_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='File_Name',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='result',
            name='Habitat_features_visible',
            field=models.CharField(choices=[('Snow_cover_1–50%', 'Snow cover 1–50%'), ('Snow_cover_50–100%', 'Snow cover 50–100%'), ('Water', 'Water'), ('Burn_area', 'Burn area'), ('Human_signs', 'Human signs'), ('None', 'None of the above')], max_length=20),
        ),
        migrations.AlterField(
            model_name='result',
            name='Observer_Name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='result',
            name='What_is_the_PREDOMINANT_vegetation',
            field=models.CharField(choices=[('Poor_visibility', 'Poor visibility of predominant vegetation'), ('Alpine_Tundra', 'Alpine Tundra'), ('Lichen/Moss/Herbaceous', 'Lichen/Moss/Herbaceous'), ('Shrubby', 'Shrubby'), ('Forested–Deciduous', 'Forested – Deciduous'), ('Forested–Coniferous', 'Forested – Coniferous'), ('Unvegetated_Areas', 'Unvegetated Areas')], max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='What_part_of_the_habitat_is_visible',
            field=models.CharField(choices=[('Ground_immediate_surroundings', 'Ground and immediate surroundings'), ('None', 'None'), ('Only_ground', 'Only ground')], max_length=35),
        ),
    ]
