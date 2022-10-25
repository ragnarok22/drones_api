# Generated by Django 3.2.16 on 2022-10-25 16:17

import apps.drones.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='drone_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='drone', to='drones.drone'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='model',
            field=models.CharField(choices=[('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Cruiserweight', 'Cruiserweight'), ('Heavyweight', 'Heavyweight')], max_length=100),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')], max_length=50),
        ),
        migrations.AlterField(
            model_name='drone',
            name='weight_limit',
            field=models.IntegerField(validators=[apps.drones.validators.weight_limit_validator]),
        ),
        migrations.AlterField(
            model_name='medication',
            name='code',
            field=models.CharField(max_length=255, validators=[apps.drones.validators.medication_code_validator]),
        ),
        migrations.AlterField(
            model_name='medication',
            name='name',
            field=models.CharField(max_length=255, validators=[apps.drones.validators.medication_name_validator]),
        ),
    ]