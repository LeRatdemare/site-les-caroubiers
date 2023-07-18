from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Family(models.Model):

    name = models.CharField(max_length=50, unique=True)
    has_child_in_college = models.BooleanField(default=False)
    has_child_in_school = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

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