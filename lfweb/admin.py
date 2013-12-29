from django.contrib import admin
from models import Collection, Yarn, News, Gallery
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    list_display = ( 'title','abstract','text','pub','pub_order',)
    date_hierarchy = 'date'
    prepopulated_fields = {'slug':('title',),}
    list_filter = ('pub',)
		
    
admin.site.register(News, NewsAdmin)

class YarnInline(admin.TabularInline):
    model = Yarn

class CollectionAdmin(TranslationAdmin):
	list_display = ('parent','name','title','abstract','description','pub','pub_order',)
	prepopulated_fields = {'slug':('name',),}
	#inlines = [YarnInline, ]

admin.site.register(Collection, CollectionAdmin)

class YarnAdmin(TranslationAdmin):
	list_display = ('name','icon','pub','pub_order','collection')
	list_filter = ('collection','pub',)
	exclude = ('title',)

	def name(self,obj):
		return obj.name
	name.allow_tags = True	

	def icon(self, obj):
		return '<img title="%s" src="/media/%s" style="height: 42px; border-radius: 5px; -webkit-border-radius: 5px;" />' % (obj.title, obj.img)
	icon.allow_tags = True        

admin.site.register(Yarn, YarnAdmin)

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)