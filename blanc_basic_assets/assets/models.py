from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    file = models.ImageField('Image', upload_to='assets/image',
            height_field='image_height', width_field='image_width')
    image_height = models.PositiveIntegerField(editable=False)
    image_width = models.PositiveIntegerField(editable=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url


class File(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    file = models.FileField(upload_to='assets/file')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url
