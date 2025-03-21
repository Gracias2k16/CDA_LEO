/*//////////////////////////////////////////////////////////////////////
///////////////////////    Fonction menu glissant //////////////////////
//////////////////////////////////////////////////////////////////////*/

 // Sélection des éléments
 const menu = document.getElementById("menuOverlay");
 const openBtn = document.getElementById("Txt_menu");
 const closeBtn = document.getElementById("closeMenu");

 // Ouvrir le menu
 openBtn.addEventListener("click", function() {
     menu.classList.add("active");
 });

 // Fermer le menu
 closeBtn.addEventListener("click", function() {
     menu.classList.remove("active");
 });

 // Fermer en cliquant en dehors du menu
 document.addEventListener("click", function(event) {
     if (!menu.contains(event.target) && !openBtn.contains(event.target)) {
         menu.classList.remove("active");
     }
 });

 /*//////////////////////////////////////////////////////////////////////
////////////////////    Fonction Selection moteur  //////////////////////
//////////////////////////////////////////////////////////////////////*/

let valeurMoteur = 0;
    const boutons = document.querySelectorAll(".Choix_Moteur_Selection");

    boutons.forEach(bouton => {
        bouton.addEventListener("click", function() {
            // Supprimer la classe 'selected' de tous les boutons
            boutons.forEach(btn => btn.classList.remove("selected"));

            // Ajouter la classe 'selected' au bouton cliqué
            this.classList.add("selected");

            // Mettre à jour la variable valeur
            valeurMoteur = this.getAttribute("data-value");
            console.log("Valeur sélectionnée =", valeurMoteur);
        });
    });

 /*//////////////////////////////////////////////////////////////////////
////////////////////    Fonction Selection moteur  //////////////////////
//////////////////////////////////////////////////////////////////////*/

let valeurBoite = 0;
    const boutonsBoite = document.querySelectorAll(".Choix_Boite_Selection");

    boutonsBoite.forEach(bouton => {
        bouton.addEventListener("click", function() {
            // Supprimer la classe 'selected' de tous les boutons
            boutonsBoite.forEach(btn => btn.classList.remove("selected2"));

            // Ajouter la classe 'selected' au bouton cliqué
            this.classList.add("selected2");

            // Mettre à jour la variable valeur
            valeurBoite = this.getAttribute("data-value");
            console.log("Valeur sélectionnée =", valeurBoite);
        });
    });

/*//////////////////////////////////////////////////////////////////////
////////////////////    Fonction Curseur sélection //////////////////////
//////////////////////////////////////////////////////////////////////*/

////////////////////  Curseur KM MAX //////////////////////

let valeurKM = 1; // Variable qui stocke la valeur du curseur
    const curseur = document.getElementById("curseur_KM");
    const affichage_KM = document.getElementById("valeur-affichee_KM");

    curseur.addEventListener("input", function() {
        valeurKM = this.value; // Met à jour la variable avec la valeur du curseur
        affichage_KM.textContent = "Valeur : " + valeurKM; // Affiche la valeur en temps réel
        console.log("Valeur sélectionnée_KM =", valeurKM); // Affiche la valeur dans la console
    });

////////////////////  Curseur PUSSIANCE //////////////////////

const minRange = document.getElementById("minRange");
const maxRange = document.getElementById("maxRange");
const rangeValues = document.getElementById("range-values");

minRange.addEventListener("input", updateRange);
maxRange.addEventListener("input", updateRange);

function updateRange() {
    let minValue = parseInt(minRange.value);
    let maxValue = parseInt(maxRange.value);

    // Empêcher min d'aller au-dessus de max et vice versa
    if (minValue >= maxValue) {
        minRange.value = maxValue - 1;
    }
    if (maxValue <= minValue) {
        maxRange.value = minValue + 1;
    }

    rangeValues.textContent = `Min : ${minRange.value} | Max : ${maxRange.value}`;
}

/*//////////////////////////////////////////////////////////////////////
////////////////////    Fonction selection presta //////////////////////
//////////////////////////////////////////////////////////////////////*/

const buttons = document.querySelectorAll(".selection-btn");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            // Désactive tous les boutons
            buttons.forEach(btn => btn.classList.remove("active"));
            // Active le bouton cliqué
            button.classList.add("active");
        });
    });

/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage Presta1   //////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const buttonElement = document.getElementById('Offre_WW'); // Sélection par ID
    const pElement = document.querySelector('.Offre_WW_texte'); // Sélection par la classe

    console.log('Le script est bien chargé et exécuté');

    buttonElement.addEventListener('click', () => {
        console.log('Clic sur le h3 détecté');
        
        if (pElement.style.display === 'none' || pElement.style.display === '') {
            pElement.style.display = 'block'; // Affiche le texte
            console.log('Le texte a été affiché');

        } else {
            pElement.style.display = 'none'; // Cache le texte
            console.log('Le texte a été caché');
        }
    });
});