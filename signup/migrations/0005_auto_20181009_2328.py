# Generated by Django 2.0.4 on 2018-10-09 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20181009_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='firt_name',
            new_name='first_name',
        ),
    ]
