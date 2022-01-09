from django.http import response
from django.shortcuts import render
from .models import Moduls, lessons, booksall as book
from django.http import FileResponse, HttpResponse
# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Test, classinline, natijalar, TestModul


# from . import models

def home(request):
    dat1 = Test.objects.all()
    for i in dat1.all():
        # for i2 in dat1.all():
        print(i, '+++++++++++++++++')
    dat = Test.objects.filter(num=4)
    for i in dat:
        op = classinline.objects.filter(test_key=i)
        for da in op:
            daq = da.option
    # print(daq)

    context = {

    }
    return render(request, 'index.html', context)


def register_login_view(request):
    context = {

    }
    return render(request, 'auth_template/auth_index.html', context)


def auoth_index(request):
    context = {

    }
    return render(request, 'dashboard_templates/index.html', context)


def dashboard_about(request):
    context = {

    }
    return render(request, 'dashboard_templates/about.html', context)


def dashboar_article(request):
    return render(request, 'dashboard_templates/article.html')


def dashboard_sertificate(request):
    return render(request, 'dashboard_templates/certificates.html')


def dashboard_pasword_change(request):
    return render(request, 'dashboard_templates/dashboard-password-change.html')


def dashboard(request):
    return render(request, 'dashboard_templates/dashboard.html')


def documents(request):
    return render(request, 'dashboard_templates/documents.html')


def help_handbook(request):
    return render(request, 'dashboard_templates/help-handbook.html')


def info(request):
    user = request.user.id
    kurs = Moduls.objects.filter(users=user)
    context = {
        'kurs': kurs
    }

    return render(request, 'dashboard_templates/info.html', context)


def info_prezentatsiya(request, id, id1):
    lesson = lessons.objects.filter(moduls_key=id, num=id1)
    lesson1 = lessons.objects.filter(moduls_key=id)
    # tepada books modelmini as qilib book ga tenglab oldim chuniki def funksiyalarimda 
    books1 = book.objects.filter(modul_key=id)
    # if books1:
    #     print('dsa')
    # for data in lesson1:
    #     d = data.prizentatsiya
    # print(d)
    modul_id = id

    context = {
        'lesson': lesson,
        'lessons': lesson1,
        'm_id': modul_id,
        'books1': books1,

    }
    return render(request, 'dashboard_templates/prezentatsiya.html', context)


def videos(request):
    return render(request, 'dashboard_templates/videos.html')


def poisk(request):
    return render(request, 'dashboard_templates/poisk.html')


def stoer(request, id):
    modul_id = id
    books = book.objects.filter(modul_key=modul_id)

    paginator = Paginator(books, 55)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
        'm_id': modul_id,
        'books': contacts,
    }

    return render(request, 'dashboard_templates/store-inner.html', context)


def books(request):
    return render(request, 'dashboard_templates/store-inner.html')


def open(request, id):
    booka = book.objects.filter(id=id)
    for i in booka:
        d = i.book
    response = FileResponse(d)
    # response['Content-Disposition'] = '; filename="shartnoma.pdf"'
    return response

    # return response


from .models import Test
from .form import NatijaForm


def test(request):
    global h, g
    test1 = Test.objects.filter(test_key=1).order_by('?')
    test = TestModul.objects.filter(id=1)
    test3 = TestModul.objects.get(id=1)

    for i in test:
        soat = int(i.test_time) * 3600
        min = int(i.test_time) * 60
    answers = []
    for i in test1:
        a = i.id
        answer = request.GET.get(f'test-{a}')
        answers.append(answer)

    option = []
    for i in test1:
        option.append(i.answer)
    g = 0
    h = 0
    print(option)
    print(answers)
    d = 0

    for a in option:
        if option[g] == answers[g]:
            h = h + 1
            d = 1
        g = g + 1
    print(h)

    context = {
        "test1": test1,
        "test": test,
        "soat": soat,
        'min': min,
        'da': d

    }
    return render(request, 'dashboard_templates/test.html', context)


def result(request):
    # if request.method == 'GET':
    #     answers = []
    #     a = 1
    #     if test1 != None:
    #         for i in test1:
    #             answer = request.GET.get(f'test-{a}')
    #             answers.append(answer)
    #             a = a + 1
    #
    #     print(answers)
    #     print(request.body)
    #     option = []
    #     for i in Test.objects.all():
    #         option.append(i.answer)
    #     g = 0
    #     h = 0
    #     for a in option:
    #         if answers[g] != None:
    #             if option[g] == answers[g]:
    #                 h = h + 1
    #         g = g + 1
    #     print(h)

    return redirect('info')
