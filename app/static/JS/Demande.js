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
///////////////////////    Message FLash   //////////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const messages = document.querySelectorAll(".flash_message");
    messages.forEach(function(message) {
        setTimeout(function() {
            message.style.display = "none"; // Masquer le message après 3 secondes
        }, 4000);
    });
});

/*//////////////////////////////////////////////////////////////////////
////////////////////    Fonction Selection moteur  //////////////////////
//////////////////////////////////////////////////////////////////////*/

let valeurMoteur = "";
    const boutons = document.querySelectorAll(".Choix_Moteur_Selection");
    const hiddenInput = document.getElementById("hidden_moteur");

    boutons.forEach(bouton => {
        bouton.addEventListener("click", function() {
            // Supprimer la classe 'selected' de tous les boutons
            boutons.forEach(btn => btn.classList.remove("selected"));

            // Ajouter la classe 'selected' au bouton cliqué
            this.classList.add("selected");

            // Mettre à jour la variable valeur
            valeurMoteur = this.getAttribute("data-value");
            hiddenInput.value = valeurMoteur;
            console.log("Valeur sélectionnée =", valeurMoteur);
        });
    });

 /*//////////////////////////////////////////////////////////////////////
////////////////////    Fonction Selection BOITE  //////////////////////
//////////////////////////////////////////////////////////////////////*/

let valeurBoite = 0;
    const boutonsBoite = document.querySelectorAll(".Choix_Boite_Selection");
    const hiddenInputBoite = document.getElementById("hidden_boite");

    boutonsBoite.forEach(bouton => {
        bouton.addEventListener("click", function() {
            // Supprimer la classe 'selected' de tous les boutons
            boutonsBoite.forEach(btn => btn.classList.remove("selected2"));

            // Ajouter la classe 'selected' au bouton cliqué
            this.classList.add("selected2");

            // Mettre à jour la variable valeur
            
            valeurBoite = this.getAttribute("data-value");
            hiddenInputBoite.value = valeurBoite;
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
    const champCacheKM = document.getElementById("km_max");

    curseur.addEventListener("input", function() {
        valeurKM = this.value; // Met à jour la variable avec la valeur du curseur
        affichage_KM.textContent = "Valeur : " + valeurKM; // Affiche la valeur en temps réel
        champCacheKM.value = valeurKM;
    });

////////////////////  Curseur PUSSIANCE //////////////////////


const maxRange = document.getElementById("maxRange");
const puissanceMax = document.getElementById("puissance_max");
const rangeValues = document.getElementById("range-values");

    function updateRange() {
        const maxValue = parseInt(maxRange.value);
        puissanceMax.value = maxValue;
        rangeValues.textContent = `Max : ${maxValue}`;
    }

    maxRange.addEventListener("input", updateRange);

    // Initialisation
    updateRange();

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

document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll('.selection-btn');
    const champType = document.getElementById("type_prestation");
    let dernierAffiche = null;

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const id = button.getAttribute("data-id");
            const pElement = document.querySelector(`.Offre_WW_texte[data-id="${id}"]`);

            champType.value = id;

            if (dernierAffiche && dernierAffiche !== pElement) {
                dernierAffiche.style.display = 'none'; // Cache l'ancien texte
            }

            if (pElement.style.display === 'none' || pElement.style.display === '') {
                pElement.style.display = 'block'; // Affiche le texte du bouton cliqué
                dernierAffiche = pElement;
            }
        });
    });
});
/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage CONTINUER   //////////////////
//////////////////////////////////////////////////////////////////////*/


document.addEventListener("DOMContentLoaded", () => {
    const buttonContinuer = document.querySelector(".Continuer");
    const suiteDiv = document.querySelector("#Deuxeme_partie");
    const inputPrestation = document.querySelector("#type_prestation");

    buttonContinuer.disabled = true; // Désactivé par défaut
    suiteDiv.style.display = "none";

    // Observer le champ caché pour activer le bouton
    const observer = new MutationObserver(() => {
        if (inputPrestation.value !== "") {
            buttonContinuer.disabled = false;
        }
    });

    observer.observe(inputPrestation, {
        attributes: true,
        attributeFilter: ['value']
    });

    buttonContinuer.addEventListener("click", () => {
        buttonContinuer.classList.toggle("active");

        suiteDiv.style.display = (suiteDiv.style.display === "none" || suiteDiv.style.display === "")
            ? "block"
            : "none";

        if (suiteDiv.style.display === "block") {
            const champNomRue = document.querySelector("[name='id_Nom_rue']");
            if (champNomRue) champNomRue.focus();

            suiteDiv.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});