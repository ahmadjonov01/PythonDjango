# from ckeditor_uploader.views import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.forms import FileField


# from study_website.pages.views import test
# from .dict import DictionaryField

class News(models.Model):
    class Meta:
        verbose_name = 'Yangiliklar'

    title = models.CharField(max_length=20000, verbose_name='Sarlavha')
    sub_title = models.CharField(max_length=20000, verbose_name='Anons')
    image = models.FileField(upload_to='static/foto_news/')
    content = models.TextField(verbose_name='Mazmuni')


class Moduls(models.Model):
    class Meta:
        verbose_name = 'Moduls'

    image = models.FileField(upload_to='static/foto_modul/')
    title = models.CharField(max_length=9999999, verbose_name='Modul nomi')
    sub_title = models.CharField(max_length=200000, verbose_name='Modul haqida qisqacha ma`lumotlar')
    users = models.ManyToManyField(User, verbose_name="O`quvchilar", blank=True)

    def __str__(self):
        return str(self.title)


class lessons(models.Model):
    class Meta:
        verbose_name = 'Darslar'

    num = models.IntegerField()
    moduls_key = models.ForeignKey('Moduls', models.CASCADE, verbose_name='Qaysi Modulga tegishli??')
    theme = models.CharField(max_length=20000, verbose_name='MAVZU')
    prizentatsiya = models.FileField(upload_to='static/prizentatsiya_powerPoint', blank=True)
    video1 = models.FileField(upload_to='static/video_lessons', blank=True)
    video2 = models.FileField(upload_to='static/video_lessons', blank=True)
    content = models.TextField(verbose_name='Mavzu maruzasi haqida', blank=True)

    def __str__(self):
        return str(self.num) + ')' + self.theme + '  Modul ' + self.moduls_key.title


# class books(models.Model):
#     book_choise = [
#         ('Ilmiy maqola', 'Ilmiy maqola'),
#         ('Kitob', 'Kitob'),
#         ('Maqola', 'Maqola'),
#     ]
#     modul_key  = models.ForeignKey('Moduls', models.CASCADE,verbose_name='KURS NOMI')
#     lesson_key  = models.ForeignKey('lessons', models.CASCADE, verbose_name='Dars')
#     book = models.FileField(upload_to='static/books')
#     book_type = models.CharField(max_length=100,choices=book_choise,verbose_name='Ma`lumot noma turi',default='Kitob')
#     date = models.DateField(auto_now_add=True,verbose_name='Yuklangan sana')

class booksall(models.Model):
    book_choise = [
        ('Ilmiy maqola', 'Ilmiy maqola'),
        ('Kitob', 'Kitob'),
        ('Maqola', 'Maqola'),
    ]
    modul_key = models.ForeignKey('Moduls', models.CASCADE, verbose_name='KURS NOMI')
    # lesson_key  = models.ForeignKey('lessons', models.CASCADE, verbose_name='Dars')
    book_name = models.CharField(max_length=2000, verbose_name='Ma`lumot nomi')
    book = models.FileField(upload_to='static/books')
    book_type = models.CharField(max_length=100, choices=book_choise, verbose_name='Ma`lumot noma turi',
                                 default='Kitob')
    date = models.DateField(auto_now_add=True, verbose_name='Yuklangan sana')

    # def __str__(self):
    #     return self.modul_key.


class TestModul(models.Model):
    class Meta:
        verbose_name = 'Test modul'

    CHOICES = [
        ('soat', 'soat'),
        ('min', 'min'),
    ]
    moduls_test_key = models.ForeignKey(Moduls, models.CASCADE, verbose_name='Test Moduli')
    test_theme = models.CharField(max_length=200, verbose_name='Test mavzusi')
    test_author = models.CharField(max_length=200, verbose_name='Test aftori')
    date = models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana')
    time = models.CharField(choices=CHOICES, max_length=20, verbose_name='Vaqtini belgilang')
    test_time = models.CharField(max_length=200, verbose_name='Test yechish uchun berilgan vaqt')
    time_time = models.TimeField()

    def __str__(self):
        return self.test_theme


class Test(models.Model):
    class Meta:
        verbose_name = 'Test'

    test_key = models.ForeignKey(TestModul, models.CASCADE, verbose_name='Test Moduli')
    num = models.IntegerField()
    question = models.CharField(max_length=2000, verbose_name='Savollar')
    option1 = models.CharField(max_length=200, verbose_name='Birinchi Javob')
    option2 = models.CharField(max_length=200, verbose_name='Ikkinchi Javob')
    option3 = models.CharField(max_length=200, verbose_name='Uchunchi Javob')
    option4 = models.CharField(max_length=200, verbose_name='To`rtinchi Javob')

    answer = models.CharField(max_length=200, verbose_name='To`g`ri Javob')

    def __str__(self):
        return str(self.num)


class classinline(models.Model):
    test_key = models.ForeignKey(Test, on_delete=models.CASCADE)
    option = models.CharField(max_length=220)


class natijalar(models.Model):
    class Meta:
        verbose_name = 'Natijalar'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Test1 = models.ForeignKey(TestModul, on_delete=models.CASCADE)
    test_alls = models.IntegerField(verbose_name='Testlar soni')
    test_t = models.IntegerField(verbose_name='Testdagi to`g`ri javoblar soni')

    # def __str__(self):
    #     return str(self.Test1)


from ckeditor.fields import RichTextField


class Ckeditor:
    content = RichTextField()
