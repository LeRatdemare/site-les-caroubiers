from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Family(models.Model):

    name = models.CharField(max_length=50, unique=True)
    has_child_in_college = models.BooleanField(default=False)
    has_child_in_school = models.BooleanField(default=False)
    total_participations = models.IntegerField()

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
    periode = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    categorie = models.CharField(choices=Categorie.choices, max_length=10)
    datetime = models.DateTimeField(auto_now=True)
    commentaire = models.CharField(max_length=1500, blank=True)

class CreneauInscription(models.Model):
    semaine = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(52)])
    jour = models.CharField(choices=Jour.choices, max_length=15)
    creneau = models.CharField(choices=Creneau.choices, max_length=10)
    horaire_arrivee = models.TimeField(blank=True, null=True)
    horaire_depart = models.TimeField(blank=True, null=True)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)

# --------------------------------- FIN INSCRIPTIONS

# class Periode(models.Model):

#     name = models.CharField(max_length=50, unique=True)
#     number_of_weeks = models.IntegerField(default=9, validators=[MinValueValidator(1), MaxValueValidator(12)])

# class TimeSlot(models.Model):
    
#     class Slot(models.TextChoices):
#         MATIN = 'matin'
#         MIDI = 'midi'
#         SOIR = 'soir'
    
#     # periode = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # P1 à P5
#     # week_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(52)]) # S1 à S52
#     # day_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # Day1 à Day5
#     date = models.DateField() # Il faudra calculer la période, la semaine et le jour à partir de ça
#     slot = models.CharField(choices=Slot.choices, max_length=10)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     family = models.ForeignKey(Family, null=True, on_delete=models.SET_NULL) # ex : DEFAYE
#     team_member = models.CharField(max_length=50) # ex : Arnaud DEFAYE

# class Holydays(models.Model):
    
#     date = models.DateField()