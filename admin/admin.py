from django.contrib import admin
from admin import models


# Register your models here.
class uesradmin1(admin.ModelAdmin):
    list_display = ['pid', 'pwd', 'age', 'brith']


admin.site.register(models.useradmin, uesradmin1)
