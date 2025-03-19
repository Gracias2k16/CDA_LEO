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