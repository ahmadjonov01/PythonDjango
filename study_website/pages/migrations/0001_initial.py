# Generated by Django 3.2.5 on 2022-01-08 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20000, verbose_name='Sarlavha')),
                ('sub_title', models.CharField(max_length=20000, verbose_name='Anons')),
                ('image', models.FileField(upload_to='static/foto_news/')),
                ('content', models.TextField(verbose_name='Mazmuni')),
            ],
            options={
                'verbose_name': 'Yangiliklar',
            },
        ),
        migrations.CreateModel(
            name='Moduls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='static/foto_modul/')),
                ('title', models.CharField(max_length=9999999, verbose_name='Modul nomi')),
                ('sub_title', models.CharField(max_length=200000, verbose_name='Modul haqida qisqacha ma`lumotlar')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='O`quvchilar')),
            ],
            options={
                'verbose_name': 'Moduls',
            },
        ),
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('theme', models.CharField(max_length=20000, verbose_name='MAVZU')),
                ('prizentatsiya', models.FileField(blank=True, upload_to='static/prizentatsiya_powerPoint')),
                ('video1', models.FileField(blank=True, upload_to='static/video_lessons')),
                ('video2', models.FileField(blank=True, upload_to='static/video_lessons')),
                ('content', models.TextField(blank=True, verbose_name='Mavzu maruzasi haqida')),
                ('moduls_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.moduls', verbose_name='Qaysi Modulga tegishli??')),
            ],
            options={
                'verbose_name': 'Darslar',
            },
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.FileField(upload_to='static/books')),
                ('book_type', models.CharField(choices=[('Ilmiy maqola', 'Ilmiy maqola'), ('Kitob', 'Kitob'), ('Maqola', 'Maqola')], default='Kitob', max_length=100, verbose_name='Ma`lumot noma turi')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yuklangan sana')),
                ('lesson_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.lessons', verbose_name='Dars')),
            ],
        ),
    ]
