from django.contrib import admin
from .models import NonVegClassicModel
# Register your models here.
class NonVegClassicAdmin(admin.ModelAdmin):
    list_display = ['Pizza','Small','Medium','Large']

admin.site.register(NonVegClassicModel,NonVegClassicAdmin)