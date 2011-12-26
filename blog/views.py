# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render_to_response
from _tea.blog.models import Entry, Category

from datetime import datetime

def index(request):
    if not request.session.get('bred'):
        request.session['bred'] = 'disabled'
    if request.method == 'GET' and request.GET.get('bred') == 'enable':
        request.session['bred'] = 'enabled'
    elif request.method == 'GET' and request.GET.get('bred') == 'disable':
        request.session['bred'] = 'disabled'

    bred = request.session.get('bred')
    entry_list = Entry.objects.filter(date_publication__lte=datetime.now()).exclude(id__exact=13)

    paginator = Paginator(entry_list, 5, 2)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    #tags = 0 #(entry_list, Category.objects.get(id=entry_list[]))
    return render_to_response('index.html', {'entry_list': entries, 'categories': categories, 'bred': bred })

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
