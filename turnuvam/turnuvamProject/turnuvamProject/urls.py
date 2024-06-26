"""
URL configuration for turnuvamProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
from django.urls import path, include #include modülünü import ediyoruz
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.anasayfa,name="anasayfa"),
    path('users/',include('users.urls')),
    path('tournaments/',include('tournaments.urls')),
    path('games/<int:gameId>',include('tournaments.urls')),
    path('login/',views.user_login,name="login"),
    path('register/',views.user_register,name="register"),
    path('logout/',views.user_logout,name="logout"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
