# Generated by Django 2.0.6 on 2020-09-16 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api3', '0004_auto_20200916_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='School',
            new_name='school',
        ),
    ]