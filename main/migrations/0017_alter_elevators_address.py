# Generated by Django 3.2.5 on 2021-07-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_elevators_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevators',
            name='address',
            field=models.CharField(max_length=255, unique=True, verbose_name='Адрес'),
        ),
    ]