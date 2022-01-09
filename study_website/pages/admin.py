from django.contrib import admin
from django.db.models import fields
from .models import News, Moduls, lessons, booksall, Test, classinline, natijalar,TestModul
from django import forms
from ckeditor.widgets import CKEditorWidget


class ColorsInLine(admin.StackedInline):
    model = classinline
    fields = ['option']
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ['num']
    inlines = [ColorsInLine]


# class lessonsAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())

    # class Meta:TestModul
    #     model = lessons

# def test(request):
#     test1 = Test.objects.all().order_by('?')
#     test = TestModul.objects.filter(id=1)
#     for i in test:
#         soat = int(i.test_time) * 3600
#         min = int(i.test_time) * 60
#     print(soat)
#     context = {
#         "test1": test1,
#         "test": test,
#         "min": str(min),
#         "soat": str(soat),
#
#     }
class lessonsAdmin(admin.ModelAdmin):
    form = lessons

admin.site.register(News)
admin.site.register(Moduls)
admin.site.register(lessons)
admin.site.register(booksall)
admin.site.register(Test, NewsAdmin)
admin.site.register(natijalar)
admin.site.register(TestModul)
