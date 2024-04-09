from django.contrib import admin
from .models import Games


class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Games,GamesAdmin)
