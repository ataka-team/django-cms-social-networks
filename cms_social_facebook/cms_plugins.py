from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_social_facebook import models

class FacebookCommentsPlugin(CMSPluginBase):
    model = models.FacebookComments
    name = 'Social Facebook Comments Plugin'
    render_template = 'cms_social_facebook/comments.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'comments': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookCommentsPlugin)
