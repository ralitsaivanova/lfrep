from django import template
from lfweb.models import HomepageVideo

register = template.Library()

def mmenu_class(value):
    if value == 1:
        return "one"
    if value == 2:
        return "two"
    if value == 3:
        return "three"
    if value == 4:
        return "four"
    
register.filter('mmenu_class', mmenu_class)    

def mmenu_img(value):
    if value == 1:
        return "lfweb/img/bg-azienda.jpg"
    if value == 2:
        return "bg-cashmere.jpg"
    if value == 3:
        return "bg-qualita.jpg"
    if value == 4:
        return "bg-contatti.jpg"
    
register.filter('mmenu_img', mmenu_img) 

def background_class(value):
    
    value = int(value)
    if value == 4:
        return 'storia'

    if value == 6:
        return 'mission'
        
    if value == 15:
        return 'filaecarda'
        
    if value == 14:
        return 'certiependa'
        
    if value == 21:
        return 'red'
        
    if value == 'filiera':
        return 'filiera'
        
    if value == 8:
        return 'news'
        
    if value == 26:
        return 'sedi'                             
    
register.filter('background_class', background_class)   
    

@register.inclusion_tag('lfweb/tags/homepage_video.html')
def homepage_video():
    video = HomepageVideo.objects.filter(pub=True)[0]  
    return {'video':video}