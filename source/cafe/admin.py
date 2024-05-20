from django.contrib import admin
from django.db.models.signals import pre_save

from taggit.models import Tag
from taggit.admin import TagAdmin

from .models import Product, RuTag
from source.services import prepoplated_slug


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.unregister(Tag)
@admin.register(RuTag)
class RuTagAdmin(TagAdmin):
    pre_save.connect(prepoplated_slug, sender=RuTag)
