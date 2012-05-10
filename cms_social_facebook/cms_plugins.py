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

class FacebookFacepilePlugin(CMSPluginBase):
    model = models.FacebookFacepile
    name = 'Social Facebook Facepile Plugin'
    render_template = 'cms_social_facebook/facepile.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'facepile': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookFacepilePlugin)

class FacebookLikeboxPlugin(CMSPluginBase):
    model = models.FacebookLikebox
    name = 'Social Facebook Likebox Plugin'
    render_template = 'cms_social_facebook/likebox.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'likebox': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLikeboxPlugin)

class FacebookLikePlugin(CMSPluginBase):
    model = models.FacebookLike
    name = 'Social Facebook Like Plugin'
    render_template = 'cms_social_facebook/like.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'like': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLikePlugin)


