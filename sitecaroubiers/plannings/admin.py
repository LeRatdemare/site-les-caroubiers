from django.contrib import admin 
from plannings.models import Family, Inscription, CreneauInscription, Periode

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_child_in_college', 'has_child_in_school', 'total_participations')
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'categorie', 'prenom', 'famille', 'periode', 'datetime')
class CreneauInscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'inscription', 'semaine', 'jour', 'creneau')
class PeriodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'annee', 'numero', 'nb_semaines')

# Register your models here.
admin.site.register(Family, FamilyAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(CreneauInscription, CreneauInscriptionAdmin)
admin.site.register(Periode, PeriodeAdmin)