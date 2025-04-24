from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField

from wagtail.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


NEW_TABLE_OPTIONS = {
    "minSpareRows": 0,
    "startRows": 4,
    "startCols": 4,
    "colHeaders": False,
    "rowHeaders": True,
    "contextMenu": [
        "row_above",
        "row_below",
        "---------",
        "col_left",
        "col_right",
        "---------",
        "remove_row",
        "remove_col",
        "---------",
        "undo",
        "redo",
    ],
    "editor": "text",
    "stretchH": "all",
    "renderer": "text",
    "autoColumnSize": False,
}


class HomePage(Page):
    lead_text = models.CharField(
        "소개글", max_length=255, blank=True, help_text="Text to describe the page"
    )
    button = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        help_text="옵션선택",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=500,
        default="Read More",
        blank=False,
        help_text="Button text",
    )

    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="배너 배경 이미지",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="배너 배경 이미지",
    )

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
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        FieldPanel("banner_background_image"),
        FieldPanel("body"),
    ]
