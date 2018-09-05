from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from contact_form.forms import PotentialForm


@plugin_pool.register_plugin
class ContactFormPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "contact_form/b-contact-form.html"
    cache = False

    def render(self, context, instance, placeholder):
        form = PotentialForm()
        context['form'] = form
        context = super(ContactFormPlugin, self).render(context, instance, placeholder)
        return context
