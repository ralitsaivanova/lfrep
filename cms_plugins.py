from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.models import Text
from cms.plugins.text.forms import TextForm

class PlainTextPlugin(CMSPluginBase):
        model = Text
        name = _("PlainText")
        form = TextForm
        render_template = "cms/plugins/text.html"

        def render(self, context, instance, placeholder):
                context.update({
                        'body': instance.body, 
                        'placeholder': placeholder,
                        'object': instance
                })
                return context
        
        def save_model(self, request, obj, form, change):
                obj.clean_plugins()
                super(PlainTextPlugin, self).save_model(request, obj,
        form, change)

plugin_pool.register_plugin(PlainTextPlugin)