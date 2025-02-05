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
            message.style.display = "none"; // Masquer le message après 4 secondes
        }, 4000);
    });
});