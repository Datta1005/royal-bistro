from django.contrib import admin
from .models import ClassicInfoModel
# Register your models here.
class ClassicInfoAdmin(admin.ModelAdmin):
    list_display = ['Pizza','Small','Medium','Large']

admin.site.register(ClassicInfoModel,ClassicInfoAdmin)
# Register your models here.

# Register your models here.
