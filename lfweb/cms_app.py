from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class LfwebHook(CMSApp):
    name = _("LfwebHook")
    urls = ["lfweb.urls"]

apphook_pool.register(LfwebHook)