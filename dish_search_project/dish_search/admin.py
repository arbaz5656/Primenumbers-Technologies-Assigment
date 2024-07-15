from django.contrib import admin
from . models import Restaurant

@admin.register(Restaurant)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id','name')


# Register your models here.
