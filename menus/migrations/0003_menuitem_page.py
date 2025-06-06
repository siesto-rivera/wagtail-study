# Generated by Django 5.1.8 on 2025-04-24 22:48

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0002_menuitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="page",
            field=modelcluster.fields.ParentalKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="menu_items",
                to="menus.menu",
            ),
            preserve_default=False,
        ),
    ]
