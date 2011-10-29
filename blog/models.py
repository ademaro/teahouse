# -*- coding: utf-8 -*-
from django.db import models

from pyadmin import verbose_name_cases, verbose_name_field_cases

class Category(models.Model):
    name = models.CharField(verbose_name = verbose_name_field_cases(u'категория', sort = u"категории"), max_length=250, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = verbose_name_cases(u"категория", (u"категория", u"категории", u"категории"),
            gender = 0, change = u"категорию", delete = u"категорию", add = u"категорию")
        verbose_name_plural = verbose_name.plural

class Entry(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    alias = models.SlugField(verbose_name='Алиас для url', null=True, blank=True, unique=True)
    text  = models.TextField(verbose_name='Текст', blank=True, help_text='Use Markdown syntax.')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    date_publication = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.title, self.category)

    class Meta:
        ordering = ['-date_publication']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
