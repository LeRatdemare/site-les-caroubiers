from django.contrib import admin 
from plannings.models import Family, Inscription, CreneauInscription

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'has_child_in_college', 'has_child_in_school', 'total_participations')
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'categorie', 'prenom', 'famille', 'periode', 'datetime')
class CreneauInscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'inscription', 'semaine', 'jour', 'creneau')

# Register your models here.
admin.site.register(Family, FamilyAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(CreneauInscription, CreneauInscriptionAdmin)