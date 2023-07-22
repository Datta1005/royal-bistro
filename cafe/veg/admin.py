from django.contrib import admin
from .models import VegInfoModel
# Register your models here.
class VegInfoAdmin(admin.ModelAdmin):
    list_display = ['Burger','prize']

admin.site.register(VegInfoModel,VegInfoAdmin)
# Register your models here.
