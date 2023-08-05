from plannings.models import Family, Inscription, CreneauInscription
from plannings.python_scripts.functions import *

def generate_empty_periode(nb_semaines = 10, premiere_semaine=36):
    """
    Génère les semaines avec tous les jours de la semaine et tous les créneaux de base.
    """
    # TODO Faudra récupérer les vraies dates de début/fin de période
    periode = {
        'datedebut': '2023-09-01',
        'datefin': '2023-10-27',
        'semaines': []
    }
    # On rajoute les semaines dans la période
    for num_semaine in range(premiere_semaine, premiere_semaine + nb_semaines):
        semaine = {
            'numero_semaine_annuel': num_semaine,
            'jours': {}
        }
        # On rajoute les jours dans la semaine
        for jour_label in ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']:
            jour = { }
            # On rajoute les créneaux dans le jour
            for creneau_label in ['matin', 'midi', 'soir']:
                creneau = {
                    'ecole': {
                        'enfants': [],
                        'equipiers': []
                    },
                    'college': {
                        'enfants': [],
                        'equipiers': []
                    }
                }
                jour[creneau_label] = creneau
                # On rajoute le champ optionnel
                if creneau_label == 'matin':
                    jour[creneau_label]['ecole']['heure_arrivee_premier_enfant'] = '08:00'
                    jour[creneau_label]['college']['heure_arrivee_premier_enfant'] = '08:00'
                elif creneau_label == 'soir':
                    jour[creneau_label]['ecole']['heure_depart_dernier_enfant'] = '18:00'
                    jour[creneau_label]['college']['heure_depart_dernier_enfant'] = '18:00'

            semaine['jours'][jour_label] = jour
        periode['semaines'].append(semaine)
    return periode

# TODO
def filled_periode_with_inscriptions(num_periode):
    periode = generate_empty_periode()
    # On commence par récupérer les inscriptions de la db
    inscriptions_ecole = extraire_donnees_creneaux(num_periode, college=False)
    inscriptions_college = extraire_donnees_creneaux(num_periode)
    for creneau in inscriptions_ecole:
        # On va récupéree le créneau correspondant de la periode
        # periode['semaines'][]
        ...
    ...

def effective_planning_for_periode(num_periode):
    ...
