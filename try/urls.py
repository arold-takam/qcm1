from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('home1',views.home1,name='home1'),
    path('profile',views.profile,name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('submit_answers/',views.submit_answers,name='submit_answers'),
    path('correction/',views.correction,name='correction'),
    path('inscription/',views.inscription,name='inscription'),
    path('conection/',views.conection,name='conection'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
