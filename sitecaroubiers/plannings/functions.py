from django.shortcuts import get_object_or_404
from plannings.models import Family
from plannings.forms import FamilyForm

def create_family(request, create_form):
    # Si le formulaire est valide
    create_form = FamilyForm(request.POST)
    if create_form.is_valid():
        # On vérifie que la famille n'existe pas déjà avant de l'enregistrer
        try:
            duplicatedFamily = get_object_or_404(Family, name=create_form.cleaned_data['name'])
            message = "La famille " + duplicatedFamily.name + " existe déjà..."
        except:
            # create_form.cleaned_data['name'] = create_form.cleaned_data['name'].upper()
            create_form.save()
        create_form = FamilyForm()
    return message