from django.contrib import admin

from .models import Food, Entry


class FoodList(admin.ModelAdmin):
    list_display = ('food_name',)
    list_filter = ('food_name',)
    search_fields = ('food_name',)
    ordering = ['food_name']


class EntryList(admin.ModelAdmin):
    list_display = ('entryID',)
    list_filter = ('entryID',)
    search_fields = ('entryID',)
    ordering = ['entryID']





admin.site.register(Food, FoodList)
admin.site.register(Entry, EntryList)
