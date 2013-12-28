from django.contrib import admin
from models import Collection, Yarn, News, Gallery
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    list_display = ( 'title','abstract','text','pub','pub_order',)
    date_hierarchy = 'date'
    prepopulated_fields = {'slug':('title',),}
    
admin.site.register(News, NewsAdmin)

class YarnInline(admin.TabularInline):
    model = Yarn

class CollectionAdmin(TranslationAdmin):
	list_display = ('parent','name','title','abstract','description','pub','pub_order',)
	prepopulated_fields = {'slug':('name',),}
	#inlines = [YarnInline, ]
        
   

admin.site.register(Collection, CollectionAdmin)

class YarnAdmin(TranslationAdmin):
	list_display = ('name','title','pub','pub_order',)
    
admin.site.register(Yarn, YarnAdmin)

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)