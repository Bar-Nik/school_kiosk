from django.contrib import admin
from .models import *


class Raspisanie_Post_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class Raspisanie_New_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class Raspisanie_Calls_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Raspisanie_Post, Raspisanie_Post_Admin)
admin.site.register(Raspisanie_New, Raspisanie_New_Admin)
admin.site.register(Raspisanie_Calls, Raspisanie_Calls_Admin)
