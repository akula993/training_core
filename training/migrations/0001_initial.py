# Generated by Django 4.2 on 2023-05-01 21:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('cud', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('cud', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='LessonVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'mov'])])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_videos', related_query_name='lesson_video', to='training.course')),
            ],
            options={
                'verbose_name': 'Видеоурок',
                'verbose_name_plural': 'Видеоуроки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='LessonText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_texts', related_query_name='lesson_text', to='training.course')),
            ],
            options={
                'verbose_name': 'Текстовый урок',
                'verbose_name_plural': 'Текстовые уроки',
                'ordering': ['title'],
            },
        ),
    ]
