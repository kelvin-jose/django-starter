# Generated by Django 2.0.4 on 2018-09-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20180913_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='regno',
            field=models.CharField(max_length=10),
        ),
    ]
