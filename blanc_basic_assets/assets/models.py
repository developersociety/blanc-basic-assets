from django.db import models


class ImageCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'image categories'

    def __unicode__(self):
        return self.title


class Image(models.Model):
    category = models.ForeignKey(ImageCategory)
    title = models.CharField(max_length=100, db_index=True)
    file = models.ImageField('Image', upload_to='assets/image',
            height_field='image_height', width_field='image_width')
    image_height = models.PositiveIntegerField(editable=False)
    image_width = models.PositiveIntegerField(editable=False)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url


class FileCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'file categories'

    def __unicode__(self):
        return self.title


class File(models.Model):
    category = models.ForeignKey(FileCategory)
    title = models.CharField(max_length=100, db_index=True)
    file = models.FileField(upload_to='assets/file')

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url
