# Generated by Django 2.0.6 on 2020-09-16 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api3', '0002_auto_20200916_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='School',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api3.School'),
        ),
    ]
