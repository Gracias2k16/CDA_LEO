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

let valeur = 0; // Initialisation de la variable

    document.getElementById("Choix_Moteur_Selection").addEventListener("click", function() {
        this.style.backgroundColor = "red"; // Changer la couleur
        valeur = 1; // Mettre la variable à 1
        console.log("Valeur =", valeur); // Afficher dans la console
    });