from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms.utils import ErrorList
from wagtail import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock


class MyTitleBlock(blocks.StructBlock):

    text = blocks.CharBlock(required=True, help_text="Text to display")

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class LinkValue(blocks.StructValue):
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(max_length=100, default="More details")
    internal_page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_link = value.get("external_link")
        errors = {}
        if internal_page and external_link:
            errors["internal_page"] = ErrorList(
                [
                    "Both of these fields cannot be filled. Please select or enter only one option."
                ]
            )
            errors["external_link"] = ErrorList(
                [
                    "Both of these fields cannot be filled. Please select or enter only one option."
                ]
            )
        elif not internal_page and not external_link:
            errors["internal_page"] = ErrorList(
                ["Please select a page or enter a URL for one of these options."]
            )
            errors["external_link"] = ErrorList(
                ["Please select a page or enter a URL for one of these options."]
            )

        if errors:
            raise blocks.StreamBlockValidationError(errors)

        return super().clean(value)


class MyCard(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100)
    text = blocks.TextBlock(max_length=234)
    image = ImageChooserBlock()
    link = Link(help_text="내부 또는 외부 링크 선택")


class MyCardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(MyCard())

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(choices=self.field.widget.choices)


class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    # image_alignment = blocks.ChoiceBlock(
    image_alignment = RadioSelectBlock(
        choices=[
            ("left", "Left"),
            ("right", "Right"),
        ],
        default="left",
    )
    title = blocks.CharBlock(max_length=60, help_text="...")
    text = blocks.TextBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image with Text"


class CallToActionBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=200, help_text="Max length of 200 characters.")
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"
        icon = "plus"
        label = "Call to Action"


class PricingTableBlock(TableBlock):
    class Meta:
        template = "streams/pricing_table_block.html"
        label = "Pricing Table"
        icon = "table"
        help_text = "Table with pricing information"


class RichTextWithTitleBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=100)
    content = blocks.RichTextBlock()

    class Meta:
        template = "streams/simple_richtext_block.html"
        icon = "edit"
        label = "Rich Text with Title"
