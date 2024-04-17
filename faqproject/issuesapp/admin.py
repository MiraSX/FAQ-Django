from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
