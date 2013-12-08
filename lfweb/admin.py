from django.contrib import admin
from models import Collection, Yarn, News, Gallery
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    list_display = ( 'title','abstract','text','pub','pub_order',)
    date_hierarchy = 'date'
    prepopulated_fields = {'slug':('title',),}
    
admin.site.register(News, NewsAdmin)

class CollectionAdmin(TranslationAdmin):
    pass

admin.site.register(Collection, CollectionAdmin)

class YarnAdmin(TranslationAdmin):
    pass

admin.site.register(Yarn, YarnAdmin)

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)