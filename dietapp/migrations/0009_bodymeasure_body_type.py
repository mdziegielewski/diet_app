# Generated by Django 2.1.4 on 2018-12-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietapp', '0008_auto_20181217_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodymeasure',
            name='body_type',
            field=models.SmallIntegerField(choices=[(1, 'ektomorfik'), (2, 'mezomorfik'), (3, 'endomorfik')], default=0),
            preserve_default=False,
        ),
    ]
