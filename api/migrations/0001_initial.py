# Generated by Django 2.0.6 on 2020-09-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_work', models.BooleanField(default=True)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'other')], default=0)),
                ('tell', models.CharField(max_length=20)),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic')),
            ],
            options={
                'verbose_name': '狗蛋的员工',
                'verbose_name_plural': '狗蛋的员工',
                'db_table': 'zhf_emp',
            },
        ),
    ]