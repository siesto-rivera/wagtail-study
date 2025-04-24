from django.db import models
from wagtail.admin.panels import FieldPanel

# from wagtail.bin import wagtail

from wagtail.blocks import RichTextBlock

from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock
from home.models import NEW_TABLE_OPTIONS
from streams import blocks
from streams.blocks import RichTextWithTitleBlock, ImageAndTextBlock


class FlexPage(Page):

    body = StreamField(
        [
            ("title", blocks.MyTitleBlock()),
            ("cards", blocks.MyCardsBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("cta", blocks.CallToActionBlock()),
            (
                "testimonial",
                SnippetChooserBlock(
                    target_model="testimonials.Testimonial",
                    template="streams/testimonial_block.html",
                ),
            ),
            (
                "pricing_table",
                blocks.PricingTableBlock(table_options=NEW_TABLE_OPTIONS),
            ),
            (
                "richtext",
                RichTextBlock(
                    template="streams/simple_richtext_block.html",
                    features=[
                        "h1",
                        "h2",
                        "h3",
                        "bold",
                        "italic",
                        "ol",
                        "ul",
                        "hr",
                        "link",
                        "document-link",
                    ],
                ),
            ),
            (
                "large_image",
                ImageChooserBlock(
                    icon="image",
                    template="streams/large_image_block.html",
                    help_text="crop imagesize to 1200x775",
                ),
            ),
            # ("richtext", RichTextWithTitleBlock() ),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flex (misc) Page"
        verbose_name_plural = "Flex (misc) Pages"
