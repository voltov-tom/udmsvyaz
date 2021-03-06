# Generated by Django 3.2.5 on 2021-07-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210706_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevators',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='communication_type',
            field=models.CharField(max_length=50, verbose_name='Тип связи'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='elevator',
            field=models.CharField(max_length=50, verbose_name='Лифт №'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='entrance',
            field=models.CharField(max_length=2, verbose_name='Подъезд'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='house',
            field=models.CharField(max_length=4, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='station_type',
            field=models.CharField(max_length=50, verbose_name='Станция'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Улица'),
        ),
    ]
