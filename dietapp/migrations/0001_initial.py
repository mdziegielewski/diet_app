# Generated by Django 2.1.4 on 2018-12-15 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('age', models.SmallIntegerField()),
                ('gender', models.SmallIntegerField(choices=[(1, 'female'), (2, 'male')])),
                ('chest_measure', models.SmallIntegerField()),
                ('waist_measure', models.SmallIntegerField()),
                ('hips_measure', models.SmallIntegerField()),
                ('thigh_measure', models.SmallIntegerField()),
                ('upper_arm_measure', models.SmallIntegerField()),
                ('person_goal', models.SmallIntegerField(choices=[(1, 'utrata wagi'), (2, 'utrzymanie wagi'), (3, 'przybranie na wadze')])),
                ('physical_activity', models.SmallIntegerField(choices=[(1, 'Znikoma (brak ćwiczeń, lekka praca)'), (2, 'Bardzo mała (ćwiczenia raz na tydzień)'), (3, 'Umiarkowana (ćwiczenia 2-3 razy w tygodniu)'), (4, 'Duża (trening kilka razy w tygodniu)'), (5, 'Bardzo duża (trening kilka razy w tygodniu, praca fizyczna)')])),
                ('person_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MealNutrients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutrients_name', models.CharField(max_length=64)),
                ('kcal', models.SmallIntegerField()),
                ('protein', models.SmallIntegerField()),
                ('carbohydrates', models.SmallIntegerField()),
                ('saturated_fats', models.SmallIntegerField()),
                ('unsaturated_fat', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MealRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=128)),
                ('meal_recipe', models.TextField()),
                ('meal_preparation_time', models.CharField(max_length=16)),
                ('meal_photo', models.FileField(upload_to='')),
                ('meal_ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dietapp.MealNutrients')),
            ],
        ),
    ]
