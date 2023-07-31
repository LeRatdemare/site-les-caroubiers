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
        genererPlanningEquipiers(planningsJson['college']);
        genererPlanningEquipiers(planningsJson['ecole'], false); // On précise que ce n'est pas le collège
    },
    error: function (xhr, status, error) {
        console.error(error);
    }
});

// Prend un paramètre l'un des 2 plannings (école ou collège), se réferrer à la vue 'get_base_plannings'
function genererPlanningEquipiers(planning, college = true) {
    // On déclare la div du template dans laquelle vont se greffer les périodes
    let blockId = (college ? 'college' : 'ecole') + '-equipiers-div'
    let planningBlock = document.getElementById(blockId);

    // On parcours la liste des périodes (P1, P2, etc...)
    for (periodName in planning) {
        // Déclaration des variables pour la période en cours
        let periodCurrentId = blockId + '-' + periodName
        let periodDiv = document.createElement("div"); // Div qui contient la période
        semaines = planning[periodName]['semaines']; // Liste d'objets JSON [{lundi:..., mardi:...,...},{...},...]
        // Paramètrage de la div
        // periodDiv.innerHTML = periodName;
        periodDiv.setAttribute("class", "period-div");
        periodDiv.setAttribute("id", periodCurrentId);
        planningBlock.appendChild(periodDiv) // On attache la période dans sa div parent
        // endPlanning.parentNode.insertBefore(periodDiv, endPlanning); // Pour insérer avant un tag
        // On parcours la période semaine par semaine
        for (numSemaine in semaines) { // On parcours la liste des semaines
            // On déclare les variables pour la semaine en cours
            weekCurrentId = periodCurrentId + '-W' + numSemaine
            semaine = semaines[numSemaine]; // Au format {lundi:..., mardi:..., etc...}
            let weekTab = document.createElement("table");
            // Paramètrage du tableau
            // weekTab.innerHTML = "Semaine " + numSemaine;
            // Création du header
            weekTableHead = document.createElement("thead");
            weekTableBody = document.createElement("tbody");
            weekHeadRow = document.createElement("tr");
            weekTableHeadTitle = document.createElement("th");
            weekTableHeadTitle.innerHTML = ("Semaine " + numSemaine)
            weekHeadRow.appendChild(weekTableHeadTitle);
            weekTableHeadMatin = document.createElement("th");
            weekTableHeadMatin.innerHTML = ("Matin")
            weekHeadRow.appendChild(weekTableHeadMatin);
            weekTableHeadMidi = document.createElement("th");
            weekTableHeadMidi.innerHTML = ("Midi")
            weekHeadRow.appendChild(weekTableHeadMidi);
            weekTableHeadSoir = document.createElement("th");
            weekTableHeadSoir.innerHTML = ("Soir")
            weekHeadRow.appendChild(weekTableHeadSoir);
            // Ajout du header et du body dans le tableau
            weekTableHead.appendChild(weekHeadRow);
            weekTab.appendChild(weekTableHead);
            weekTab.appendChild(weekTableBody);

            weekTab.setAttribute("class", "week-div");
            weekTab.setAttribute("id", weekCurrentId);
            periodDiv.appendChild(weekTab);
            // On parcours la semaine jour par jour
            for (numJour in semaine['jours']) {
                // Variables du jour
                jourName = semaine['jours'][numJour]['label'];
                dayCurrentId = weekCurrentId + '-' + jourName;
                jour = semaine['jours'][numJour]; // Au format {matin:..., midi:..., soir:...}
                let dayRow = document.createElement("tr");
                dayLabelTableData = document.createElement("td");
                dayLabelTableData.innerHTML = jourName;
                dayRow.appendChild(dayLabelTableData);
                // Paramètrage de la div
                // dayRow.innerHTML = jourName;
                // dayDiv.setAttribute("class", "day-div");
                dayRow.setAttribute("id", dayCurrentId);
                weekTableBody.appendChild(dayRow);
                // On parcours le jour créneau par créneau
                // console.log(jour)
                for (slotName of ["matin", "midi", "soir"]) {
                    // Initialisation des variables du slot
                    // Paramètrage du td
                    let slotTableData = document.createElement("td");
                    slotCurrentId = dayCurrentId + '-' + slotName;
                    slotTableData.setAttribute("id", slotCurrentId);
                    try {
                        slot = jour[slotName]; // Au format {equipiers:...,heure_arrivee_premier_enfant:...} (si matin)
                        slotTableData.innerHTML = slot['equipiers'].length;
                        dayRow.appendChild(slotTableData);
                    }
                    catch (err) {
                        slotTableData.innerHTML = "-";
                        dayRow.appendChild(slotTableData);
                        continue;
                    }
                    // // slotDiv.setAttribute("class", "slot-div");
                    // // On parcours le créneau équipier par équipier
                    // for (numEquipier in slot['equipiers']) {
                    //     // Initialisation des variables de l'équipier
                    //     teamMemberCurrentId = slotCurrentId + '-E' + numEquipier
                    //     teamMember = slot['equipiers'][numEquipier];
                    //     let teamMemberDiv = document.createElement("div");
                    //     // Paramètrage de la div
                    //     teamMemberDiv.innerHTML = teamMember;
                    //     teamMemberDiv.setAttribute("class", "team-member-div");
                    //     teamMemberDiv.setAttribute("id", teamMemberCurrentId);
                    //     slotTableData.appendChild(teamMemberDiv);
                    // }
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

