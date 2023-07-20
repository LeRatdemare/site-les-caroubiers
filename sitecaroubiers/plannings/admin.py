from django.contrib import admin 
from plannings.models import Family, Inscription, CreneauInscription

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'has_child_in_college', 'has_child_in_school')
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'famille', 'datetime')
class CreneauInscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_inscription', 'cycle_enfant', 'periode', 'semaine', 'jour', 'creneau')

# Register your models here.
admin.site.register(Family, FamilyAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(CreneauInscription, CreneauInscriptionAdmin)