from django.db import models


class FieldMapAbstract(models.Model):
    geo_field = models.CharField(max_length=255)
    shape_field = models.CharField(max_length=255)
    mandatory = models.BooleanField(default=True)
    is_value = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s:%s" % (self.geo_field, self.shape_field)
