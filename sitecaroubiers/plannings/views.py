from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from plannings.models import Family, Inscription, CreneauInscription, Periode
from django.forms import Form
from plannings.forms import FamilyForm
import operator
from plannings.python_scripts import functions
from plannings.python_scripts import variables
from datetime import datetime
import json
from django.templatetags.static import static

# Create your views here.
def index(request):
    # print(variables.templatePlanning)
    # creneaux = functions.extraire_donnees_creneaux(1, college=False)
    # print('creneaux_dispos :', creneaux)
    # plannings = functions.generer_tous_les_plannings_possibles(creneaux)
    # print('plannings : ', plannings)
    # print('Taille :', len(plannings[0][1][0]))

    return render(request, 'pages/index.html')

def gestion_familles(request):
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
                    families = families.exclude(id=family.id)
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
    families = sorted(families, key=operator.attrgetter('name'))
    return render(request, 'pages/gestion_familles.html', {'families':families, 'create_form':create_form, 'creation_error_message':message})

def gestion_plannings(request):
    return render(request, 'pages/gestion_plannings.html')

# cible_inscription peut être soit "équipier" soit "enfant"
def inscription_perisco(request, num_periode, cible_inscription):
    families = Family.objects.all()
    templatePeriod = variables.templatePlanning['college']['P'+str(num_periode)]
    cible_inscription = cible_inscription.lower()

    if request.method == 'POST':
        # On récupère les données de l'inscription
        prenom = request.POST[cible_inscription+'-label']
        famille = get_object_or_404(Family, name=request.POST[cible_inscription+'-famille']) 
        categorie_de_linscrit = ''
        try:
            # Crée une erreur si le champ n'existe pas
            categorie_de_linscrit = request.POST['cycle']
        except:
            categorie_de_linscrit = 'EQ'
        commentaire = request.POST['commentaire']
        periode = Periode.objects.get(annee=datetime.now().year, numero=num_periode)
        # On enregistre l'inscription dans la BDD
        inscription = Inscription.objects.create(prenom=prenom, famille=famille, periode=periode, categorie=categorie_de_linscrit, commentaire=commentaire)
        # On récupère également les créneaux
        for semaine in templatePeriod['semaines']:
            numSemaine = semaine['numeroSemaineAnnuel']
            for jour in semaine['jours']:
                nomJour = jour['label']
                # On construit le nom de l'input SANS le créneau
                base_input_name = 'sem'+str(numSemaine)+'-'+jour['label']+'-'
                # Si le créneau du matin existe
                for creneau in ['matin', 'midi', 'soir']:
                    try:
                        # La ligne en dessous renverra une erreur si la
                        #checkbox n'a pas été cochée et qu'aucun horaire n'est donné.
                        input_value = request.POST[base_input_name + creneau]
                        # Si c'est juste une checkbox cochée
                        if input_value=='on':
                            CreneauInscription.objects.create(semaine=numSemaine, jour=nomJour, creneau=creneau, inscription=inscription)
                        # S'il y a un horaire de précisé
                        elif input_value != 'absent':
                            time_object = datetime.strptime(input_value, '%H:%M').time()
                            # Si on est l'après-midi, alors c'est un horaire de départ
                            if time_object > datetime.strptime('12:00', '%H:%M').time():
                                CreneauInscription.objects.create(semaine=numSemaine, jour=nomJour, creneau=creneau, inscription=inscription, horaire_depart=time_object)
                            # Sinon, c'est un horaire d'arrivée
                            else:
                                CreneauInscription.objects.create(semaine=numSemaine, jour=nomJour, creneau=creneau, inscription=inscription, horaire_arrivee=time_object)
                        # On enregistre le créneau dans la bonne table
                    except:
                        pass
    else:
        pass
    context = {
        'cible_inscription': cible_inscription,
        'families':families,
        'semaineType':variables.semaineType,
        'templatePeriod':templatePeriod
    }
    return render(request, 'pages/inscription_perisco.html', context=context)

def selection_periode(request):
    return render(request, 'pages/selection_periode.html')

def gestion_periode(request, num_periode):
    annee_rentree = datetime.now().year - (1 if num_periode>2 else 0)
    context = {'num_periode': num_periode, 'annee_scolaire': str(annee_rentree)+'/'+str(annee_rentree+1)}
    return render(request, 'pages/gestion_periode.html', context=context)

# ----------------------------------------------- JSON Infos -----------------------------------------------
def get_base_plannings(request):
    _file = open('plannings/static/json/planning_equipiers.json')
    planning_json = json.loads("".join(_file.readlines()))
    _file.close()
    print(planning_json)
    return JsonResponse(planning_json)