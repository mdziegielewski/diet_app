# Generated by Django 2.1.4 on 2018-12-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietapp', '0015_auto_20181218_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealnutrients',
            name='nutrients_group',
            field=models.SmallIntegerField(choices=[(1, 'Owoce i warzywa'), (2, 'Mięso'), (3, 'Ryby'), (4, 'Produkty zbożowe, jajka')], default=False),
        ),
    ]
