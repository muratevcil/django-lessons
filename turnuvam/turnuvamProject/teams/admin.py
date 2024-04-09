from django.contrib import admin
from .models import Teams


class TeamsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Teams, TeamsAdmin)
# Register your models here.
