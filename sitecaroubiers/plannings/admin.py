from django.contrib import admin 
from plannings.models import Family

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'has_child_in_college', 'has_child_in_school')

# Register your models here.
admin.site.register(Family, FamilyAdmin)