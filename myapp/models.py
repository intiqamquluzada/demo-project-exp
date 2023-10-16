from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    age = models.IntegerField(verbose_name="Age")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "My Model"
        verbose_name_plural = "My Model"
