# Generated by Django 3.2.5 on 2021-07-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210713_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevators',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
