from django.contrib import admin
from myapp import models


# Register your models here.
@admin.register(models.MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ["name", "version", "version_id", "version_created_at"]
    pass
