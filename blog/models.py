# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Entry(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    alias = models.SlugField(verbose_name='Алиас для url', null=True, blank=True, unique=True)
    text  = models.TextField(verbose_name='Текст', blank=True, help_text='Use Markdown syntax.')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    date_publication = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.title, self.category)

    class Meta:
        ordering = ['date_publication']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
