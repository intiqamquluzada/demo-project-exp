from django.contrib import admin
from myapp.models import MyModel, Car, Masters, CarImages, CarCategory, Category


admin.site.register(MyModel)
admin.site.register(Car)
# admin.site.register(CarCategory)
admin.site.register(Category)
admin.site.register(Masters)
admin.site.register(CarImages)
