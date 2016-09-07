from django.db.models.signals import pre_save, post_delete
from .models import Image, File


def asset_file_change(sender, instance, **kwargs):
    old_obj = sender.objects.get(pk=instance.pk)

    # Delete the old file if the file names don't match
    if old_obj.file.name != instance.file.name:
        storage = old_obj.file.storage
        storage.delete(name=old_obj.file.name)


def asset_file_delete(instance, **kwargs):
    # Remove the file along with it
    instance.file.delete(save=False)


pre_save.connect(asset_file_change, sender=Image)
pre_save.connect(asset_file_change, sender=File)
post_delete.connect(asset_file_delete, sender=Image)
post_delete.connect(asset_file_delete, sender=File)
