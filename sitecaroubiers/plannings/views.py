from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from plannings.models import Family
from django.forms import Form
from plannings.forms import FamilyForm
import operator

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def gestion(request):
    families = Family.objects.all()
    message = None
    create_form = FamilyForm()
    # Si on arrive sur la page après envoie d'un formulaire
    if request.method == 'POST':
        # print(request.POST)
        # Si c'est le formulaire de création
        if request.POST.get('is-create'):
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
        # Sinon si c'est le formulaire de modification
        elif request.POST.get('is-update'):
            rslt = request.POST
            # On regarde famille par famille s'il y a des champs modifiés
            for family in families:
                if not (rslt.get(family.name + '.delete')) is None :
                    family.delete()
                else :
                    has_child_in_school = not (rslt.get(family.name + '.has_child_in_school') is None)
                    has_child_in_college = not (rslt.get(family.name + '.has_child_in_college') is None)
                    setattr(family, 'has_child_in_school', has_child_in_school)
                    setattr(family, 'has_child_in_college', has_child_in_college)
                    family.save()
                # print(family.name + " --> " + str(has_child_in_college) + "-" + str(has_child_in_school))
        # Autres forms
        else:
            pass
    # Si méthode GET
    else:
        pass
    # Pas opti de faire 2 fois la requêtes mais nécessaire pour avoir page à jour
    families = Family.objects.all()
    families = sorted(families, key=operator.attrgetter('name'))
    return render(request, 'pages/gestion.html', {'families':families, 'create_form':create_form, 'creation_error_message':message})