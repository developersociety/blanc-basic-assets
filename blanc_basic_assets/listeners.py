from django.db.models.signals import pre_save, post_delete
from django.core.files.storage import default_storage


def asset_file_change(sender, instance, **kwargs):
    # Must be saved already
    if instance.pk is not None:
        try:
            old_obj = sender.objects.get(pk=instance.pk)

            # Delete the old file if the file names don't match
            if old_obj.file.path != instance.file.path:
                default_storage.delete(old_obj.file.path)
        except:
            pass


def asset_file_delete(sender, instance, **kwargs):
    # Try and remove the file if possible
    try:
        instance.file.delete(save=False)
    except:
        pass


pre_save.connect(asset_file_change, sender='assets.Image')
pre_save.connect(asset_file_change, sender='assets.File')
post_delete.connect(asset_file_delete, sender='assets.Image')
post_delete.connect(asset_file_delete, sender='assets.File')
