# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication')
    fields = ('title', 'alias', 'text', 'category', 'date_publication')
    filter_horisontal = ('category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
