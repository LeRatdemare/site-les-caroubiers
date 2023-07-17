from django import forms
from plannings.models import Family

class FamilyForm(forms.ModelForm):
    
    class Meta:
        model = Family
        fields = '__all__'
        labels = {
            'name': "Nom de famille",
            'has_child_in_school': "Enfant à l'école",
            'has_child_in_college': "Enfant au collège",
        }
        # exclude = ('has_child_in_school',)
