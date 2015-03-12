from django.db import models
from django.template.defaultfilters import slugify


class Coffee_item(models.Model):
        name = models.CharField(max_length=128, unique=True)
        price = models.IntegerField(default=0)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Coffee_item, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

# Create your models here.
