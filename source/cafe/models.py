from django.db import models

from taggit.models import Tag
from taggit.managers import TaggableManager, TaggedItem

from source.services import slugify as ru_slugify


class RuTag(Tag):
    """
    Тэги сохраняющие оттранслитерированные кириличные тэги
    """
    class Meta:
        proxy = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def slugify(self, tag, i=None):
        return ru_slugify(self.name)[:128]


class RuTaggedItem(TaggedItem):
    """
    хз чё
    """
    class Meta:
        proxy = True

    @classmethod
    def tag_model(cls):
        return RuTag


class Product(models.Model):
    name = models.CharField(
        max_length=55,
        verbose_name='Название'
    )
    slug = models.SlugField()
    description = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    categories = TaggableManager(through=RuTaggedItem)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)


class Category(models.Model):
    name = models.CharField(
        max_length=55,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)
