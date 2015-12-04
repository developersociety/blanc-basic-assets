from django.db.models.signals import post_delete, pre_save


def asset_file_change(sender, instance, raw, **kwargs):
    # Don't update when loading a fixutre
    if raw:
        return

    # Must be saved already
    if instance.pk is not None:
        old_obj = sender.objects.get(pk=instance.pk)

        # Delete the old file if the file names don't match
        if old_obj.file.name != instance.file.name:
            storage = old_obj.file.storage
            storage.delete(name=old_obj.file.name)


def asset_file_delete(instance, **kwargs):
    # Remove the file along with it
    instance.file.delete(save=False)


pre_save.connect(asset_file_change, sender='assets.Image')
pre_save.connect(asset_file_change, sender='assets.File')
post_delete.connect(asset_file_delete, sender='assets.Image')
post_delete.connect(asset_file_delete, sender='assets.File')
