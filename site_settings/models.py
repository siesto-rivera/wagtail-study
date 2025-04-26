from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.fields import RichTextField


@register_setting
class HoursSettings(BaseSiteSetting):
    hours = RichTextField(blank=True, null=True, features=["link"])
    panels = [FieldPanel("hours")]


@register_setting
class ContactSettings(BaseSiteSetting):
    contact = RichTextField(blank=True, null=True, features=["link"])
    panels = [FieldPanel("contact")]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_contact_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)


@register_setting
class SocialMediaSettings(BaseSiteSetting):

    facebook = models.URLField(blank=True, help_text="Enter your Facebook URL")
    twitter = models.URLField(blank=True, help_text="Enter your Twitter URL")
    youtube = models.URLField(blank=True, help_text="Enter your YouTube URL")
    instagram = models.URLField(blank=True, help_text="Enter your Instagram URL")

    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_social_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)
