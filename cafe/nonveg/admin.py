from django.contrib import admin
from .models import NonVegInfoModel
# Register your models here.
class NonVegInfoAdmin(admin.ModelAdmin):
    list_display = ['Burger','prize']

admin.site.register(NonVegInfoModel,NonVegInfoAdmin)
# Register your models here.
