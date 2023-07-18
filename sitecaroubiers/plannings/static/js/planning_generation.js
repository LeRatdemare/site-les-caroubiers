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
        genererPlanning(planningsJson['college']);
        genererPlanning(planningsJson['ecole'], false);
    },
    error: function (xhr, status, error) {
        console.error(error);
    }
});

// Prend un paramètre l'un des 2 plannings (école ou collège), se réferrer à la vue 'get_base_plannings'
function genererPlanning(planning, college = true) {
    // console.log(planning);
    for (periodName in planning) {
        // console.log(planning[period]);
        let periodDiv = document.createElement("div");
        periodDiv.innerHTML = periodName;
        periodDiv.setAttribute("class", "period-block");
        periodDiv.setAttribute("id", (college ? 'college' : 'ecole') + "-period-block-" + periodName);
        let planningBlock = document.getElementById('planning-' + (college ? 'college' : 'ecole'));
        // endPlanning.parentNode.insertBefore(periodDiv, endPlanning);
        planningBlock.appendChild(periodDiv)
        semaines = planning[periodName]['semaines'];
        for (numSemaine in semaines) {
            // console.log(planning[period]['semaines'][semaine]);
            semaine = semaines[numSemaine];
            let weekDiv = document.createElement("div");
            weekDiv.innerHTML = semaine;
            weekDiv.setAttribute("class", "week-block");
            weekDiv.setAttribute("id", (college ? 'college' : 'ecole') + "-week-block-" + numSemaine);
            periodDiv.appendChild(weekDiv);
            for (jourName in semaine) {
                // console.log(jour);
                jour = semaine[jourName];
                let dayDiv = document.createElement("div");
                dayDiv.innerHTML = jour;
                dayDiv.setAttribute("class", "day-block");
                dayDiv.setAttribute("id", (college ? 'college' : 'ecole') + "-day-block-" + jourName);
                weekDiv.appendChild(dayDiv);
                for (slotName in jour) {
                    // console.log(slot)
                    slot = jour[slotName];
                    let slotDiv = document.createElement("div");
                    slotDiv.innerHTML = slot;
                    slotDiv.setAttribute("class", "slot-block");
                    slotDiv.setAttribute("id", (college ? 'college' : 'ecole') + "-slot-block-" + slotName);
                    dayDiv.appendChild(slotDiv);
                    for (numEquipier in slot['equipiers']) {
                        equipier = slot['equipiers'][numEquipier];
                        let teamMemberDiv = document.createElement("div");
                        teamMemberDiv.innerHTML = slot;
                        teamMemberDiv.setAttribute("class", "team-member-block");
                        teamMemberDiv.setAttribute("id", (college ? 'college' : 'ecole') + "-team-member-block-" + numEquipier);
                        slotDiv.appendChild(teamMemberDiv);
                        console.log(equipier);
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

