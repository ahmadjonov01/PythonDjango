from django import urls
from django.http.request import validate_host
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_login_view, name='register_login'),
    path('dashboard/about', views.dashboard_about, name='dashboard_about'),
    path('dashboard/article', views.dashboar_article, name='dashboard_article'),
    path('dashboard/certificate', views.dashboard_sertificate, name='dashboard_certificate'),
    path('dashboard/password-change', views.dashboard_pasword_change, name='password_change'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('documents/', views.documents, name='documents'),
    path('help-handbook/', views.help_handbook, name='help_handbook'),
    path('info/', views.info , name='info'),
    path('info_prezentatsiya/<int:id><int:id1>', views.info_prezentatsiya , name='info_prezentatsiya'),
    path('videos/', views.videos , name='videos'),
    path('poisk/', views.poisk , name='poisk'),
    path('auoth_index/', views.auoth_index , name='auoth_index'),
    path('stoer/<int:id>', views.stoer , name='stoer'),
    path('books/', views.books , name='books'),
    path('open/<int:id>', views.open, name='open'),
    path('test/', views.test, name='test'),
    path('result/', views.result, name='result'),
    
    

  
   

    
    
    

    # info_prezentatsiya

]
