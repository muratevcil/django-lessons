from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
 path('', views.uyelerSayfasi), # fonksiyonu çağırıyoruz
 path('addUser/',views.uyeEkle),
 path('<int:userId>',views.userDesc),
]