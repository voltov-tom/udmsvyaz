# Generated by Django 3.2.5 on 2021-07-12 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210712_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elevators',
            name='city',
        ),
    ]
