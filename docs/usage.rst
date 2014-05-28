=====
Usage
=====


Models
======

All file and image assets are grouped by category, however by default the
Django admin and any other Django forms will only display ``ForeignKey`` fields
as a single list. To make asset selection easier in forms, use the
``AssetForeignKey`` field instead as a drop-in replacement for ``ForeignKey``.

For images::

    from django.db import models
    from blanc_basic_assets.fields import AssetForeignKey

    class Album(models.Model):
        title = models.CharField(max_length=100)
        image = AssetForeignKey('assets.Image')

For files, an optional example::

    from django.db import models
    from blanc_basic_assets.fields import AssetForeignKey

    class Post(models.Model):
        title = models.CharField(max_length=100)
        attachment = AssetForeignKey('assets.File', null=True, blank=True)
