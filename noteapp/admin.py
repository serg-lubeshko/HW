from django.contrib import admin

from .models import *


# Register your models here.
# Добавим поля в админку

class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category",'created_at', 'update_at', 'is_published')
    list_display_links = ("id", "title")
    search_fields = ('title', 'content')


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name")
    search_fields = ('name',)


admin.site.register(Note, NoteAdmin)  # Внимание! порядок регистрации классов важен
admin.site.register(MainCategory, MainCategoryAdmin)

