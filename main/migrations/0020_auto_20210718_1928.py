# Generated by Django 3.2.5 on 2021-07-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_elevators_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevators',
            name='comment',
            field=models.TextField(default='нет данных', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='elevators',
            name='communication_type',
            field=models.CharField(default='нет данных', max_length=255, verbose_name='Тип связи'),
        ),
    ]
