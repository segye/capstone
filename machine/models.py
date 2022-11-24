from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/women_top_reference_person_test/')

    class Meta:
        ordering = ['id']