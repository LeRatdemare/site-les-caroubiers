/* Les checkbox ont des id au format 'semType-lundi-matin'
ou 'sem36-mardi-soir' pour les autres semaines. */

// Initialisation des variables
let nbSemainesInYear = 52 // Ici on triche, on fera beaucoup trop de calculs mais ça simplifie le code
let joursSemaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'];
let creneauxPossibles = ['matin', 'midi', 'soir'];
// Pour chaque checkbox de la semaine type
for (let jour of joursSemaine) {
    for (let creneau of creneauxPossibles) {
        // On lui rajoute un listener qui sera appelé lorsqu'il sera coché/décoché
        checkboxId = "semType-" + jour + "-" + creneau;
        checkbox = document.getElementById(checkboxId);
        if (checkbox) {
            checkbox.addEventListener('input', function (event) {
                // On donne sa valeur à tous les créneau pour le reste de la semaine
                setAllSlotsOfPeriod(jour, creneau, this.checked)
            });
        }
    }
}

function setAllSlotsOfPeriod(jour, creneau, valeur) {
    // Pour chaque semaine de l'année
    for (let numSemaine = 1; numSemaine <= nbSemainesInYear; numSemaine++) {
        // On récupère l'id du créneau correspondant
        checkboxId = "sem" + numSemaine + "-" + jour + "-" + creneau;
        checkbox = document.getElementById(checkboxId);
        // Si le créneau existe, on le coche
        if (checkbox) {
            checkbox.checked = valeur
        }
    }
}
