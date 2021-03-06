# Generated by Django 2.0.6 on 2020-09-16 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('course_name', models.CharField(max_length=128)),
                ('hours', models.IntegerField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': '课程表',
                'verbose_name_plural': '课程表',
                'db_table': 'zhf_course',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('school_name', models.CharField(max_length=128)),
                ('pic', models.ImageField(default='img/1.jpg', upload_to='img')),
                ('address', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
                'db_table': 'zhf_press',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('teacher_name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
                'db_table': 'zhf_teacher',
            },
        ),
        migrations.CreateModel(
            name='TeacherDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=11)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='api3.Teacher')),
            ],
            options={
                'verbose_name': '教师详情',
                'verbose_name_plural': '教师详情',
                'db_table': 'zhf_teacher_detail',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='School',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api3.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(db_constraint=False, related_name='courses', to='api3.Teacher'),
        ),
    ]
