from django.shortcuts import render
from django.http import HttpResponse
def uyelerSayfasi(request):
 return HttpResponse("The page that contains users.")
def uyeEkle(request):
 return HttpResponse("The page that lets you add new users.")
def userDesc(request,userId):
 return HttpResponse('You have requested the number '+str(userId)+' user.')