# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category, Entry

import settings
media = settings.MEDIA_URL

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication')
    fields = ('title', 'alias', 'text', 'category', 'date_publication')
    filter_horisontal = ('category')

#    class Media:
#      js = ('/js/jquery.js', '/js/wymeditor/jquery.wymeditor.js','/js/editor.js')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
