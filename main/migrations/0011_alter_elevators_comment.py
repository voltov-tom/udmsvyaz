# Generated by Django 3.2.5 on 2021-07-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_elevators_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevators',
            name='comment',
            field=models.TextField(default='нет данных', verbose_name='Комментарий'),
        ),
    ]
