const thisScript = document.getElementById("plannings-construct")
let planningsJson;
// Bloc de code AJAX copié collé pour récupérer des données JSON générées par la vue 
$.ajax({
    url: thisScript.dataset.planningsUrl,  // URL de votre vue Django qui renvoie les données
    method: 'GET',
    dataType: 'json',
    success: function (response) {
        planningsJson = response;
        // Utilisez la variable dans votre script JavaScript
        console.log(planningsJson);
        // Génération des divs de gestion du planning à partir des données JSON
        genererPlanning(planningsJson['college']);
        genererPlanning(planningsJson['ecole'], false); // On précise que ce n'est pas le collège
    },
    error: function (xhr, status, error) {
        console.error(error);
    }
});

// Prend un paramètre l'un des 2 plannings (école ou collège), se réferrer à la vue 'get_base_plannings'
function genererPlanning(planning, college = true) {
    // On déclare la div du template dans laquelle vont se greffer les périodes
    let blockId = (college ? 'college' : 'ecole') + '-div'
    let planningBlock = document.getElementById(blockId);

    // On parcours la liste des périodes (P1, P2, etc...)
    for (periodName in planning) {
        // Déclaration des variables pour la période en cours
        let periodCurrentId = blockId + '-' + periodName
        let periodDiv = document.createElement("div"); // Div qui contient la période
        semaines = planning[periodName]['semaines']; // Liste d'objets JSON [{lundi:..., mardi:...,...},{...},...]
        // Paramètrage de la div
        periodDiv.innerHTML = periodName;
        periodDiv.setAttribute("class", "period-div");
        periodDiv.setAttribute("id", periodCurrentId);
        planningBlock.appendChild(periodDiv) // On attache la période dans sa div parent
        // endPlanning.parentNode.insertBefore(periodDiv, endPlanning); // Pour insérer avant un tag
        // On parcours la période semaine par semaine
        for (numSemaine in semaines) { // On parcours la liste des semaines
            // On déclare les variables pour la semaine en cours
            weekCurrentId = periodCurrentId + '-W' + numSemaine
            semaine = semaines[numSemaine]; // Au format {lundi:..., mardi:..., etc...}
            let weekDiv = document.createElement("div");
            // Paramètrage de la div
            weekDiv.innerHTML = numSemaine;
            weekDiv.setAttribute("class", "week-div");
            weekDiv.setAttribute("id", weekCurrentId);
            periodDiv.appendChild(weekDiv);
            // On parcours la semaine jour par jour
            for (jourName in semaine) {
                // Variables du jour
                dayCurrentId = weekCurrentId + '-' + jourName
                jour = semaine[jourName]; // Au format {matin:..., midi:..., soir:...}
                let dayDiv = document.createElement("div");
                // Paramètrage de la div
                dayDiv.innerHTML = jourName;
                dayDiv.setAttribute("class", "day-div");
                dayDiv.setAttribute("id", dayCurrentId);
                weekDiv.appendChild(dayDiv);
                // On parcours le jour créneau par créneau
                for (slotName in jour) {
                    // Initialisation des variables du jour
                    slotCurrentId = dayCurrentId + '-' + slotName
                    slot = jour[slotName]; // Au format {equipiers:...,heure_arrivee_premier_enfant:...} (si matin)
                    let slotDiv = document.createElement("div");
                    // Paramètrage de la div
                    slotDiv.innerHTML = slotName;
                    slotDiv.setAttribute("class", "slot-div");
                    slotDiv.setAttribute("id", slotCurrentId);
                    dayDiv.appendChild(slotDiv);
                    // On parcours le créneau équipier par équipier
                    for (numEquipier in slot['equipiers']) {
                        // Initialisation des variables de l'équipier
                        teamMemberCurrentId = slotCurrentId + '-E' + numEquipier
                        teamMember = slot['equipiers'][numEquipier];
                        let teamMemberDiv = document.createElement("div");
                        // Paramètrage de la div
                        teamMemberDiv.innerHTML = teamMember;
                        teamMemberDiv.setAttribute("class", "team-member-div");
                        teamMemberDiv.setAttribute("id", teamMemberCurrentId);
                        slotDiv.appendChild(teamMemberDiv);
                    }
                }
            }
        }
    }
}

// Création du planning du collège


// for (let i = 0; i < 10; i++) {
//     const liElement = document.createElement("li");
//     const liText = document.createTextNode(i);
//     liElement.appendChild(liText)
//     ulTags = document.getElementsByTagName("ul")
//     for (tag of ulTags) {
//         tag.appendChild(liElement);
//     }
//     console.log(i)
// }

