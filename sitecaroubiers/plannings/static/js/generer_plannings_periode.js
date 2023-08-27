const thisScript = document.getElementById("plannings-construct")
let periodeJson;
// Bloc de code AJAX copié collé pour récupérer des données JSON générées par la vue 
$.ajax({
    url: thisScript.dataset.periodeUrl,  // URL de votre vue Django qui renvoie les données
    method: 'GET',
    dataType: 'json',
    success: function (response) {
        periodeJson = response;
        // Utilisez la variable dans votre script JavaScript
        console.log(periodeJson);
        // Génération des divs de gestion du planning à partir des données JSON
        genererPlanningEquipiers(periodeJson['semaines'][0]['jours']['lundi']['matin']);
    },
    error: function (xhr, status, error) {
        console.error(error);
    }
});

function genererPlanningEquipiers(periode) {
    // const paragraphe = document.createElement("p");
    // paragraphe.innerHTML = periode;
    const mainDiv = document.getElementById("ecole-equipiers-div");
    const paragraphe = document.createElement("ul");

    for (semaine of periode['semaines']) {
        const semaineLi = document.createElement("li");
        const semaineUl = document.createElement("ul");

        paragraphe.appendChild(semaineLi);
        semaineLi.appendChild(semaineUl);
        for (jourName in ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']) {
            // const jour = 
        }
    }
    mainDiv.appendChild(paragraphe);
}