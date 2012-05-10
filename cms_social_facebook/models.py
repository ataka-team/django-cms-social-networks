from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

COLOR_CHOICES = [
    ('light', _('light')),
    ('dark', _('dark')),
]

ACTION_CHOICES = [
    ('like', _('like')),
    ('recommend', _('recommend')),
]

LAYOUT_CHOICES = [
    ('standard', _('standard')),
    ('box_count', _('box_count')),
    ('button_count', _('button_count')),
]

FONT_CHOICES = [
    ('arial', _('arial')),
    ('tahoma', _('tahoma')),
    ('verdana', _('verdana')),
    ('segoe ui', _('segoe ui')),
    ('lucida grande', _('lucida grande')),
    ('trebuchet ms', _('trebuchet ms')),
]

class FacebookComments(CMSPlugin):
    pageurl = models.URLField(_("URL to comment on"))
    num_posts = models.PositiveSmallIntegerField(_("Number of posts"),
        default=2)
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    def __unicode__(self):
        return "Comments (%s)" % (self.pageurl)

class FacebookFacepile(CMSPlugin):
    pageurl = models.URLField(_("URL"))
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    max_rows = models.PositiveSmallIntegerField(_("Max rows"),
        default=1)

    action = models.CharField(_("Actions separate by commas"),
        default=None, null=True, blank=True)

    def __unicode__(self):
        return "Facepile (%s)" % (self.pageurl)

class FacebookLikebox(CMSPlugin):
    pageurl = models.URLField(_("URL that you like it"))

    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    height = models.PositiveSmallIntegerField(_("Height"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))

    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    border_color = models.CharField(_("Color Scheme"), default=None,
            null=True, blank=True, max_length=50)

    show_faces = models.BooleanField(_("Show faces"),
            default=True)

    stream = models.BooleanField(_("Stream"),
            default=True)

    header = models.BooleanField(_("Header"),
            default=True)

    def __unicode__(self):
        return "Likebox (%s)" % (self.pageurl)


class FacebookLike(CMSPlugin):
    pageurl = models.URLField(_("URL that you like it"))

    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))

    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES,
            default='light', max_length=50)

    action = models.CharField(_("Action"), choices=ACTION_CHOICES,
            default='like', max_length=50)

    layout = models.CharField(_("Layout"), choices=LAYOUT_CHOICES,
            default='standard', max_length=50)

    font = models.CharField(_("Font"), choices=FONT_CHOICES,
            default='arial', max_length=50)

    border_color = models.CharField(_("Color Scheme"), default=None,
            null=True, blank=True, max_length=50)

    show_faces = models.BooleanField(_("Show faces"),
            default=True)

    send = models.BooleanField(_("Send"),
            default=True)


    def __unicode__(self):
        return "Like (%s)" % (self.pageurl)

class FacebookLoginButton(CMSPlugin):
    appId = models.CharField(_("App ID"))

    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))

    show_faces = models.BooleanField(_("Show faces"),
            default=True)

    max_rows = models.PositiveSmallIntegerField(_("Max rows"),
        default=1)

    def __unicode__(self):
        return "Facebook Login Button (%s)" % (self.appId)

class FacebookLivestream(CMSPlugin):
    appId = models.CharField(_("App ID"))

    event_app_id = models.CharField(_("Event App Id"),
            help_text=_("Your Facebook application ID or API key")
            )

    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    height = models.PositiveSmallIntegerField(_("Height"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))

    always_post_to_friends =models.BooleanField(_("Always_post to friends"),
            blank=True,
            null=True,
            default=None,
            help_text=_('''If set, all user posts will always go to their
profile. This option should only be used when users' posts
are likely to make sense outside of the context of the
event.''')
            )
    xid = models.BooleanField(_("XID"),
            blank=True,
            null=True,
            default=None,
            help_text=_('''If you have multiple live stream boxes on the
same page, specify a unique `xid` for each.''')
            )
    via_url = models.URLField(_("Via Attribution URL"),
            blank=True,
            null=True,
            default=None,
            help_text=_('''The URL that users are redirected to when they
click on your app name on a status (if not specified, your
Connect URL is used).''')
            )


    def __unicode__(self):
        return "Facebook Live stream (%s)" % (self.appId)


