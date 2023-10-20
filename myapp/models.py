from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MyModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    age = models.IntegerField(verbose_name="Age")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "My Model"
        verbose_name_plural = "My Model"


class CarCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kateqoriya")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Masters(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name of repairman")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Repairman"
        verbose_name_plural = "Repairmen"


class Car(models.Model):

    cat = models.ForeignKey(CarCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Car name")
    year = models.CharField(max_length=255, verbose_name="Year of car")
    masters = models.ManyToManyField(Masters, verbose_name="Repairmen")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("year",)
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class CarImages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.car.name

    class Meta:
        verbose_name = "Car photo"
        verbose_name_plural = "Car photos"
