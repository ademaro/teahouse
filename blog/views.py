# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from _tea.blog.models import Entry, Category

from datetime import datetime

def index(request):
    entry_list = Entry.objects.all().filter(date_publication__lte=datetime.now())
    categories = Category.objects.all()
    #tags = (entry_list, Category.objects.get(id=entry_list[]))	
    return render_to_response('index.html', {'entry_list': entry_list, 'categories': categories, 'tags': tags})

def entry(request, entry_id):
    try:
      entry = Entry.objects.get(id=int(entry_id))
    except Entry.DoesNotExist:
      raise Http404()
    else:
      categories = Category.objects.all()
      tags = entry.category.all()
      return render_to_response('entry.html', {'entry': entry, 'tags': tags, 'categories': categories})

def tags(request, tag_id):
    try:
      tag = Category.objects.get(id=int(tag_id))
    except Category.DoesNotExist:
      raise Http404()
    else:
      entry_list = tag.entry_set.all()
      categories = Category.objects.all()
      return render_to_response('index.html', 
	{'entry_list': entry_list, 'categories': categories, 'category': tag})
