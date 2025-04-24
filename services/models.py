from django.core.exceptions import ValidationError
from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.models import Page


class ServiceListingPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["services.ServicePage"]
    template = "services/service_listing_page.html"
    max_count = 1

    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["services"] = ServicePage.objects.live().public()
        return context


class ServicePage(Page):
    # template: templates/services/service_page.html
    parent_page_types = ["services.ServiceListingPage"]
    subpage_types = []

    description = models.TextField(
        blank=True,
        max_length=500,
    )
    internal_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="",
        on_delete=models.SET_NULL,
    )
    external_page = models.URLField(
        blank=True,
    )
    button_text = models.CharField(
        max_length=50,
        blank=True,
    )
    service_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Service image",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        FieldPanel("service_image"),
    ]

    def clean(self):
        super().clean()
        if self.internal_page and self.external_page:
            raise ValidationError(
                {
                    "internal_page": ValidationError(
                        "Please select either an internal or external page, not both."
                    ),
                    "external_page": ValidationError(
                        "Please select either an internal or external page, not both."
                    ),
                }
            )

        if not self.internal_page and not self.external_page:
            raise ValidationError(
                {
                    "internal_page": ValidationError(
                        "Please select either an internal or external page, not both."
                    ),
                    "external_page": ValidationError(
                        "Please select either an internal or external page, not both."
                    ),
                }
            )
