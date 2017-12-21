from django.contrib import admin
from models import Collection, Yarn, News, Image, Tecnicalcard, HomepageVideo
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    list_display = ( 'title','abstract','text','pub','pub_order',)
    
    prepopulated_fields = {'slug':('title',),}
    list_filter = ('pub',)
    exclude = ('abstract',)	
    
admin.site.register(News, NewsAdmin)

class TecnicalcardInline(admin.TabularInline):
    model = Tecnicalcard

class CollectionAdmin(TranslationAdmin):
	list_display = ('parent','name','title','abstract','pub','pub_order',)
	prepopulated_fields = {'slug':('name',),}
	#inlines = [TecnicalcardInline, ]

admin.site.register(Collection, CollectionAdmin)

class YarnAdmin(TranslationAdmin):
	list_display = ('name','icon','pub','pub_order','collection')
	list_filter = ('collection','pub',)
	exclude = ('title',)

	def icon(self, obj):
		return '<img title="%s" src="/media/%s" style="height: 42px; border-radius: 5px; -webkit-border-radius: 5px;" />' % (obj.title, obj.img)
	icon.allow_tags = True        

admin.site.register(Yarn, YarnAdmin)

class HomepageVideoAdmin(admin.ModelAdmin):
	list_display = ('pub','video',)
	def video(self, obj):
		return obj.src
	video.allow_tags = True   

admin.site.register(HomepageVideo,HomepageVideoAdmin )

