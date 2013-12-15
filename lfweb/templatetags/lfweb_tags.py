from django import template

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
    