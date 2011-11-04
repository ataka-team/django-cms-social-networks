from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

COLOR_CHOICES = [
    ('light', _('light')),
    ('dark', _('dark')),
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
