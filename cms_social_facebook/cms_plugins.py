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
    name = 'Social Facebook Like Button Plugin'
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

class FacebookLoginButtonPlugin(CMSPluginBase):
    model = models.FacebookLoginButton
    name = 'Social Facebook Login Button Plugin'
    render_template = 'cms_social_facebook/loginbutton.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'loginbutton': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLoginButtonPlugin)

class FacebookLivestreamPlugin(CMSPluginBase):
    model = models.FacebookLivestream
    name = 'Social Facebook Live stream Plugin'
    render_template = 'cms_social_facebook/livestream.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'livestream': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLivestreamPlugin)


