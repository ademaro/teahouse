# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from _tea.blog.models import Entry

def index(request):
    entry_list = Entry.objects.all()
    return render_to_response('index.html', {'entry_list': entry_list})

def entry(request, entry_id):
    try:
      entry = Entry.objects.get(id=int(entry_id))
    except Entry.DoesNotExists:
      raise Http404()
    else:
      tags = entry.category.all()
      return render_to_response('entry.html', {'entry': entry, 'tags': tags})
