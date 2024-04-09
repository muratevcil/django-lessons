from django.contrib import admin
from .models import Users


class Usersadmin(admin.ModelAdmin):
    list_display = ("name", "surname", "favorite_game", "balance")


admin.site.register(Users, Usersadmin)
