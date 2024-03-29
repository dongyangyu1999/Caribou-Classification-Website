# Generated by Django 3.0.3 on 2020-03-10 16:57

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_auto_20200310_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='Potential_insect_avoidance_behavior',
        ),
        migrations.AddField(
            model_name='result',
            name='Potential_insect_avoidance_behavior',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Shook_its_head', 'Shook its head'), ('Kept_nose_Ground', 'Kept its nose still AND on the ground'), ('Scratched', 'Scratched'), ('Sought_snow_patch', 'Sought snow patch'), ('Huddled', 'Huddled'), ('None', 'None of the above')], default='', max_length=72),
        ),
        migrations.DeleteModel(
            name='Potential_insect_avoidance_behavior',
        ),
    ]
