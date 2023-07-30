from django.shortcuts import get_object_or_404, get_list_or_404
from plannings.models import Family, Inscription, CreneauInscription
from statistics import stdev
import copy
# from workalendar.europe import France

# def create_family(request, create_form):
#     # Si le formulaire est valide
#     create_form = FamilyForm(request.POST)
#     if create_form.is_valid():
#         # On vérifie que la famille n'existe pas déjà avant de l'enregistrer
#         try:
#             duplicatedFamily = get_object_or_404(Family, name=create_form.cleaned_data['name'])
#             message = "La famille " + duplicatedFamily.name + " existe déjà..."
#         except:
#             # create_form.cleaned_data['name'] = create_form.cleaned_data['name'].upper()
#             create_form.save()
#         create_form = FamilyForm()
#     return message

# france = France()
# france.add_working_days()

def extraire_donnees_creneaux(numPeriode, college=True):
    """
    Met à jour les fichiers planning_equipiers.json et planning_enfant.json
    en fonction des valeurs des inscriptions enfants et équipiers enregistrées
    dans la base de donnée.
    Ne fait aucune modification de la base de donnée.

    Return : liste au format [{'semaine':..., 'jour':..., 'creneau':..., 'nb_enfants':..., 'familles':[]}, ...]
    !!! N'effectue pas de vérification sur les inscriptions !!!
    !!! Travaille uniquement avec les données saisies même si insuffisantes !!!
    """
    # On commence par récupérer toutes les inscriptions/créneaux de la période
    _inscriptions = Inscription.objects.filter(periode=numPeriode)
    # On récupère soit les enfants à l'école soit les collégiens...
    # ...et les équipiers possiblement à disposition en fonction
    print('Inscriptions :', _inscriptions)
    inscriptions_enfants = None
    inscriptions_equipiers = None
    if college:
        inscriptions_enfants = _inscriptions.filter(categorie=Inscription.Categorie.COLLEGE)
        inscriptions_equipiers = _inscriptions.filter(categorie=Inscription.Categorie.EQUIPIER, famille__has_child_in_college=True)
    else:
        inscriptions_enfants = _inscriptions.exclude(categorie__in=[Inscription.Categorie.EQUIPIER, Inscription.Categorie.COLLEGE])
        inscriptions_equipiers = _inscriptions.filter(categorie=Inscription.Categorie.EQUIPIER, famille__has_child_in_school=True)
    creneaux_enfants = CreneauInscription.objects.filter(inscription__in=inscriptions_enfants)
    creneaux_equipiers = CreneauInscription.objects.filter(inscription__in=inscriptions_equipiers)
    # - On tri les parents par créneau à occuper (là où il y a des enfants)
    creneaux_dispos = [] # La liste à renvoyer
    # Pour chaque créneau où il y a un enfant
    for creneau in creneaux_enfants:
        # On cherche le créneau concerné dans la liste
        creneau_trouve = False
        for c_eff in creneaux_dispos:
            if c_eff['semaine']==creneau.semaine and c_eff['jour']==creneau.jour and c_eff['creneau']==creneau.creneau:
                # Si il est effectivement dedans on compte l'enfant
                c_eff['nb_enfants'] += 1
                creneau_trouve = True
        # Si on n'a pas trouvé le créneau, on le crée
        if not creneau_trouve:
            c_eff = {}
            c_eff['semaine'] = creneau.semaine
            c_eff['jour'] = creneau.jour
            c_eff['creneau'] = creneau.creneau
            c_eff['nb_enfants'] = 1
            c_eff['familles'] = []
            creneaux_dispos.append(c_eff)
            # Ensuite, pour chaque créneau dans lequel il y a un équipier
            for c_eq in creneaux_equipiers:
                # S'il correspond
                if c_eq.semaine==creneau.semaine and c_eq.jour==creneau.jour and c_eq.creneau==creneau.creneau:
                    # On ajoute sa famille dans la liste effective du créneau
                    c_eff['familles'].append(c_eq.inscription.famille)
    # Arrivé ici, on a maintenant la liste des créneaux avec le nombre d'enfant
    # ainsi que les équipiers qui s'y sont inscrit.
    return creneaux_dispos
    # Il reste alors à retirer des équipiers jusqu'à atteindre les
    # proportions enfant/équipier désirées.
    # Tant qu'on n'a pas pile le bon nombre de familles dans chaque créneau on
    # recommence à les répartir (fonction récursive)
    # On enregistre le résultat dans les fichiers json

def nb_equipiers_en_trop(creneau_dispo, categorie_enfants=Inscription.Categorie.COLLEGE, nb_enfants_par_equipier_college=10, nb_enfants_par_equipier_c1=10, nb_enfants_par_equipier_c2=10, nb_enfants_par_equipier_c3=10):
    """
    Parameter : liste au format [{'semaine':..., 'jour':..., 'creneau':..., 'nb_enfants':..., 'familles':[]}, ...]
    """
    nb_equipiers_en_trop = len(creneau_dispo['familles'])
    nb_enfants_restants = creneau_dispo['nb_enfants']
    while nb_enfants_restants > 0:
        # Pour chaque équipier on retire autant d'enfants qu'il faut
        nb_equipiers_en_trop -= 1
        if categorie_enfants == Inscription.Categorie.COLLEGE:
            nb_enfants_restants -= nb_enfants_par_equipier_college
        if categorie_enfants == Inscription.Categorie.CYCLE_1:
            nb_enfants_restants -= nb_enfants_par_equipier_c1
        if categorie_enfants == Inscription.Categorie.CYCLE_2:
            nb_enfants_restants -= nb_enfants_par_equipier_c2
        if categorie_enfants == Inscription.Categorie.CYCLE_3:
            nb_enfants_restants -= nb_enfants_par_equipier_c3
    return nb_equipiers_en_trop

def get_famille_par_participation_desc():
    return Family.objects.order_by('-total_participations')

# def implique_le_minimum_de_familles_possible(creneaux_dispos, nb_enfants_par_equipier_college=10, nb_enfants_par_equipier_c1=10, nb_enfants_par_equipier_c2=10, nb_enfants_par_equipier_c3=10):
#     """

#     """
#     ...

# def minimiser_nb_equipiers_par_creneau(creneaux_dispos):
#     """
#     Parameter : liste au format [{'semaine':..., 'jour':..., 'creneau':..., 'nb_enfants':..., 'familles':[]}, ...]
#     Return : Même liste mais avec le minimum de familles impliquées par créneau
#     """
#     # On commence par regarder s'il y a assez de personnel dans chaque créneau
#     if implique_le_minimum_de_familles_possible(creneaux_dispos):
#         return creneaux_dispos
    
#     # On récupère les données de chaque famille
#     familles = Family.objects.all()
#     ...

def ecart_type_participations(creneaux_dispos):
    participations = {}
    for creneau in creneaux_dispos:
        for famille in creneau['familles']:
            try:
                participations[famille.name] += 1
            except:
                participations[famille.name] = 1
    data = []
    for part in participations.values():
        data.append(part)
    return stdev(data)

def generer_tous_les_plannings_possibles(creneaux_dispos):
    """
    Parameter : liste au format [{'semaine':..., 'jour':..., 'creneau':..., 'nb_enfants':..., 'familles':[]}, ...]
    """
    # On va générer autant de plannings qu'il est possible d'en générer,
    # puis on gardera celui qui minimise l'écart-type des participations.
    plannings = []
    # S'il n'y a pas de créneaux dispos, on renvoie une liste vide
    if len(creneaux_dispos) < 1:
        return creneaux_dispos
    # Sinon, on récupère les informations du 1er créneau
    creneau = creneaux_dispos[0]
    print('Creneau :', creneau)
    equipiers = creneau['familles']
    # print('Equipiers :', equipiers)
    surplus_equipiers = nb_equipiers_en_trop(creneau)
    # print('Surplus :', surplus_equipiers)
    # S'il n'y a qu'un seul créneau, on renvoie juste la liste des combinaisons possibles
    if len(creneaux_dispos) == 1:
        parties = partiesliste(creneaux_dispos[0]['familles'], len(equipiers) - surplus_equipiers)
        return parties
    # Si en revanche il y a plus d'un créneau, on récupère la liste des combinaisons
    combinaisons = partiesliste(creneau['familles'], len(equipiers) - surplus_equipiers)
    # print('Combinaisons :', combinaisons)
    # On récupère le reste des créneaux
    reste = copy.deepcopy(creneaux_dispos)
    reste.remove(creneau)
    # print('Reste :', reste)
    suite_plannings_possibles = generer_tous_les_plannings_possibles(reste)
    # S'il n'y a pas de combinaison possible pour le créneau, on renvoie le reste
    if len(combinaisons) < 1:
        plannings.append([[], suite_plannings_possibles])
    # Sinon, pour chaque combinaison d'équipiers possible, on la concatène avec la liste des plannings
    # possibles sur le reste des créneaux.
    for combinaison in combinaisons:
        plannings.append([combinaison, suite_plannings_possibles])
    return plannings

# -------------------------- MATH
def partiesliste(seq, taille_parties):
    """
    Code trouvé sur https://python.jpvweb.com/python/mesrecettespython/doku.php?id=parties_ensemble
    Renvoie l'ensemble des parties de seq de tailles taille_parties. (théorie des ensembles)
    """
    p = []
    i, imax = 0, 2**len(seq)-1
    while i <= imax:
        s = []
        j, jmax = 0, len(seq)-1
        while j <= jmax:
            if (i>>j)&1 == 1:
                s.append(seq[j])
            j += 1
        if len(s)==taille_parties:
            p.append(s)
        i += 1
    return p