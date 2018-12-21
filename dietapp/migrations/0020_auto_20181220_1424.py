# Generated by Django 2.1.4 on 2018-12-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietapp', '0019_auto_20181220_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymeasure',
            name='person_goal',
            field=models.SmallIntegerField(choices=[(1, 'utrata wagi'), (2, 'utrzymanie wagi'), (3, 'przybranie na wadze')], default=False),
        ),
        migrations.AlterField(
            model_name='bodymeasure',
            name='physical_activity',
            field=models.SmallIntegerField(choices=[(1, 'Znikoma (brak ćwiczeń, lekka praca)'), (2, 'Bardzo mała (ćwiczenia raz na tydzień)'), (3, 'Umiarkowana (ćwiczenia 2-3 razy w tygodniu)'), (4, 'Duża (trening kilka razy w tygodniu)'), (5, 'Bardzo duża (trening kilka razy w tygodniu, praca fizyczna)')], default=False),
        ),
    ]