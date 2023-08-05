from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from plannings.python_scripts.plannings import generate_empty_periode

# Create your models here.
class Family(models.Model):

    name = models.CharField(max_length=50, primary_key=True)
    has_child_in_college = models.BooleanField(default=False)
    has_child_in_school = models.BooleanField(default=False)
    total_participations = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

# --------------------------------- INSCRIPTIONS
class Jour(models.TextChoices):
    LUNDI = 'lundi'
    MARDI = 'mardi'
    MERCREDI = 'mercredi'
    JEUDI = 'jeudi'
    VENDREDI = 'vendredi'
class Creneau(models.TextChoices):
    MATIN = 'matin'
    MIDI = 'midi'
    SOIR = 'soir'

class Periode(models.Model):

    numero = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    annee = models.IntegerField(validators=[MinValueValidator(2023)]) # L'année de la rentrée scolaire
    planning = models.JSONField(null=True, blank=True)
    nb_semaines = models.IntegerField(default=10, validators=[MinValueValidator(5), MaxValueValidator(13)])

# Une inscription est enregistrée lorsque le parent valide soit sur la page
# d'inscription périsco "enfant" soit sur la page "équipier."
# Les créneaux auxquels correspond l'inscription sont enregistrés dans 2 tables distinctent
# qui référencent directement l'inscription. Cela permet d'éviter les redondances
class Inscription(models.Model):
    
    class Categorie(models.TextChoices):
        CYCLE_1 = 'C1'
        CYCLE_2 = 'C2'
        CYCLE_3 = 'C3'
        COLLEGE = 'COL'
        EQUIPIER = 'EQ'
    
    prenom = models.CharField(max_length=50)
    famille = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    periode = models.ForeignKey(Periode, on_delete=models.CASCADE)
    categorie = models.CharField(choices=Categorie.choices, max_length=10)
    datetime = models.DateTimeField(auto_now=True)
    commentaire = models.CharField(max_length=1500, blank=True)

class CreneauInscription(models.Model):
    semaine = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(52)]) # On va le numero de la semaine dans le mois
    jour = models.CharField(choices=Jour.choices, max_length=15)
    creneau = models.CharField(choices=Creneau.choices, max_length=10)
    horaire_arrivee = models.TimeField(blank=True, null=True) # L'horaire correspond soit à l'arrivée soit au départ
    horaire_depart = models.TimeField(blank=True, null=True)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)

# --------------------------------- FIN INSCRIPTIONS
