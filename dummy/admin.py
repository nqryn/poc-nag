from django.contrib import admin
import models

admin.site.register(models.DummyModel)
admin.site.register(models.CharFieldModel)
admin.site.register(models.ImageFieldModel)
