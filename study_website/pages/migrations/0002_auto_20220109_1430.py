# Generated by Django 3.2.5 on 2022-01-09 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booksall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=2000, verbose_name='Ma`lumot nomi')),
                ('book', models.FileField(upload_to='static/books')),
                ('book_type', models.CharField(choices=[('Ilmiy maqola', 'Ilmiy maqola'), ('Kitob', 'Kitob'), ('Maqola', 'Maqola')], default='Kitob', max_length=100, verbose_name='Ma`lumot noma turi')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yuklangan sana')),
                ('modul_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.moduls', verbose_name='KURS NOMI')),
            ],
        ),
        migrations.CreateModel(
            name='classinline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='natijalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_alls', models.IntegerField(verbose_name='Testlar soni')),
                ('test_t', models.IntegerField(verbose_name='Testdagi to`g`ri javoblar soni')),
            ],
            options={
                'verbose_name': 'Natijalar',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('question', models.CharField(max_length=2000, verbose_name='Savollar')),
                ('option1', models.CharField(max_length=200, verbose_name='Birinchi Javob')),
                ('option2', models.CharField(max_length=200, verbose_name='Ikkinchi Javob')),
                ('option3', models.CharField(max_length=200, verbose_name='Uchunchi Javob')),
                ('option4', models.CharField(max_length=200, verbose_name='To`rtinchi Javob')),
                ('answer', models.CharField(max_length=200, verbose_name='To`g`ri Javob')),
            ],
            options={
                'verbose_name': 'Test',
            },
        ),
        migrations.CreateModel(
            name='TestModul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_theme', models.CharField(max_length=200, verbose_name='Test mavzusi')),
                ('test_author', models.CharField(max_length=200, verbose_name='Test aftori')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('time', models.CharField(choices=[('soat', 'soat'), ('min', 'min')], max_length=20, verbose_name='Vaqtini belgilang')),
                ('test_time', models.CharField(max_length=200, verbose_name='Test yechish uchun berilgan vaqt')),
                ('time_time', models.TimeField()),
                ('moduls_test_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.moduls', verbose_name='Test Moduli')),
            ],
            options={
                'verbose_name': 'Test modul',
            },
        ),
        migrations.DeleteModel(
            name='books',
        ),
        migrations.AddField(
            model_name='test',
            name='test_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.testmodul', verbose_name='Test Moduli'),
        ),
        migrations.AddField(
            model_name='natijalar',
            name='Test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.test'),
        ),
        migrations.AddField(
            model_name='natijalar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classinline',
            name='test_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.test'),
        ),
    ]
