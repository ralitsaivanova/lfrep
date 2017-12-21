from django.db import models
from django.utils.translation import ugettext_lazy as _

from tinymce.models import HTMLField



class Gallery(models.Model):
    title = models.CharField(max_length=130,verbose_name = _('title'),) 

    class Meta:
        verbose_name = _('galleries')
        verbose_name_plural = _('gallery')

class Image(models.Model):
    parent = models.ForeignKey(Gallery, null = True,verbose_name = _('gallery'))
    img = models.ImageField(upload_to="uploads/gallery",verbose_name = _('img'),)
    abstract  = models.TextField(max_length=255,verbose_name = _('abstract'),)
    pub = models.BooleanField()
    pub_order = models.SmallIntegerField(verbose_name = _('pub_order'),null=True,blank=True)

    class Meta:
        verbose_name = _('images')
        verbose_name_plural = _('image')



class Collection(models.Model):
    parent = models.ForeignKey("self", null = True,verbose_name = _('collection'),blank=True)
    name = models.CharField(max_length=130,verbose_name = _('name'),null=True,blank=True)
    title = models.CharField(max_length=130,verbose_name = _('title'),null=True,blank=True)
    slug = models.SlugField(max_length=50,verbose_name = _('slug'),null=True,blank=True)
    abstract  = HTMLField(max_length=255,verbose_name = _('abstract'),null=True,blank=True)
    description  = HTMLField(verbose_name = _('description'),null=True,blank=True)
    img = models.ImageField(upload_to="uploads/gallery",verbose_name = _('img'),null=True,blank=True)
    pittogramma = models.ImageField(upload_to="uploads/gallery",verbose_name = _('pittogramma'),null=True,blank=True)
#   gallery = models.ForeignKey(Gallery, null = True,verbose_name = _('gallery'),blank=True)
    video_url = models.CharField(max_length=130,verbose_name = _('video_url'),blank=True,null=True)
    pub = models.BooleanField(verbose_name = _('pub'))
    pub_order = models.SmallIntegerField(verbose_name = _('pub_order'),null=True,blank=True)

    class Meta:
        verbose_name = _('collections')
        verbose_name_plural = _('collection')

    def __unicode__(self):  
        return self.name



class Tecnicalcard(models.Model):
    collection = models.ForeignKey(Collection)
    alttext = models.CharField(max_length=255,verbose_name = _('alttext'),null=True,blank=True)
    img = models.ImageField(upload_to="uploads/gallery",verbose_name = _('img'),null=True,blank=True)
    pub = models.BooleanField(verbose_name = _('pub'))
    pub_order = models.SmallIntegerField(verbose_name = _('pub_order'),null=True,blank=True)

    class Meta:
        verbose_name = _('technical_card')
        verbose_name_plural = _('technical_cards')

    def __unicode__(self):  
        return self.alttext        


class Yarn(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=130,verbose_name = _('name'))
    title = models.CharField(max_length=130,verbose_name = _('title'),null=True,blank=True)
    slug = models.SlugField(max_length=50,verbose_name = _('slug'),null=True)
    img = models.ImageField(upload_to="uploads/gallery",verbose_name = _('img'),null=True,blank=True)
    pub = models.BooleanField(verbose_name = _('pub'))
    pub_order = models.SmallIntegerField(verbose_name = _('pub_order'),null=True,blank=True)

    class Meta:
        verbose_name = _('yarns')
        verbose_name_plural = _('yarn')
    def __unicode__(self):  
        return self.name    

        

class News(models.Model):
    title = models.CharField(max_length=130,verbose_name = _('title'),null=True,blank=True)
    abstract  = models.CharField(max_length=255,verbose_name = _('abstract'),null=True,blank=True)
    slug = models.SlugField(max_length=50,verbose_name = _('slug'),null=True,blank=True)	
    date_from = models.DateField(verbose_name = _('date_from'),null=True,blank=True)
    date_to = models.DateField(verbose_name = _('date_to'),null=True,blank=True)
    text = HTMLField(verbose_name = _('text'),null=True,blank=True)
    img = models.ImageField(upload_to="uploads/gallery",verbose_name = _('img'),null=True,blank=True)  
 #   gallery = models.ForeignKey(Gallery, null = True,verbose_name = _('gallery'),blank=True)
    video_url = models.CharField(max_length=130,verbose_name = _('video_url'),null=True,blank=True)
    pub = models.BooleanField(verbose_name = _('pub'))
    pub_order = models.SmallIntegerField(verbose_name = _('pub_order'),null=True,blank=True)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')


class HomepageVideo(models.Model):
    src = models.TextField(verbose_name = _('source_link'),)
    pub = models.BooleanField(verbose_name = _('pub'))

    class Meta:
        verbose_name = _('video homepage')
        verbose_name_plural = _('video homepage')        




