/* Les input ont des id au format 'semType-lundi-matin'
ou 'sem36-mardi-soir' pour les autres semaines. */

// Initialisation des variables
let nbSemainesInYear = 52 // Ici on triche, on fera beaucoup trop de calculs mais ça simplifie le code
let joursSemaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'];
let creneauxPossibles = ['matin', 'midi', 'soir'];
// Pour chaque input de la semaine type
for (let jour of joursSemaine) {
    for (let creneau of creneauxPossibles) {
        // On lui rajoute un listener qui sera appelé lorsqu'il sera coché/décoché
        inputId = "semType-" + jour + "-" + creneau;
        input = document.getElementById(inputId);
        if (input) {
            input.addEventListener('input', function (event) {
                // On donne sa valeur à tous les créneau pour le reste de la semaine
                toggleAllCheckboxesForSlots(jour, creneau, this.checked)
            });
            input.addEventListener('change', function () {
                // On donne sa valeur à tous les créneau pour le reste de la semaine
                selectOptionForSlots(jour, creneau, this.value)
                console.log(this.selectIndex)
                console.log(this.value)
            });
        }
    }
}

function toggleAllCheckboxesForSlots(jour, creneau, valeur) {
    // Pour chaque semaine de l'année
    for (let numSemaine = 1; numSemaine <= nbSemainesInYear; numSemaine++) {
        // On récupère l'id du créneau correspondant
        inputId = "sem" + numSemaine + "-" + jour + "-" + creneau;
        input = document.getElementById(inputId);
        // Si le créneau existe, on le coche
        if (input) {
            input.checked = valeur
        }
    }
}
function selectOptionForSlots(jour, creneau, optionValue) {
    // Pour chaque semaine de l'année
    for (let numSemaine = 1; numSemaine <= nbSemainesInYear; numSemaine++) {
        // On récupère l'id du créneau correspondant
        inputId = "sem" + numSemaine + "-" + jour + "-" + creneau;
        input = document.getElementById(inputId);
        // Si le créneau existe, on le coche
        if (input) {
            input.value = optionValue
        }
    }
}
