/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage texte 1   //////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const h3Element = document.getElementById('Recherche_véhicule'); // Sélection par ID
    const pElement1 = document.querySelector('.Recherche_véhicule_texte'); // Sélection par la classe
    const pElement2 = document.querySelector('.Recherche_véhicule_texte_2'); // Sélection par la classe
    const ulElement = document.getElementById('Dynamic_list');
    
    console.log('Le script est bien chargé et exécuté');

    h3Element.addEventListener('click', () => {
        console.log('Clic sur le h3 détecté');
        
        if (pElement1.style.display === 'none' || pElement1.style.display === '') {
            pElement1.style.display = 'block'; // Affiche le texte
            pElement2.style.display = 'block'; // Affiche le texte
            ulElement.style.display = 'block'; // Affiche la liste
            console.log('Le texte a été affiché');

        } else {
            pElement1.style.display = 'none'; // Cache le texte
            pElement2.style.display = 'none'; // Cache le texte
            ulElement.style.display = 'none'; // Cache la Liste
            console.log('Le texte a été caché');
        }
    });
});

/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage texte 2   //////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const h3Element = document.getElementById('controle_rapport'); // Sélection par ID
    const pElement = document.querySelector('.controle_rapport_texte'); // Sélection par la classe

    console.log('Le script est bien chargé et exécuté');

    h3Element.addEventListener('click', () => {
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

/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage texte 3   //////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const h3Element = document.getElementById('Commande_paiement'); // Sélection par ID
    const pElement = document.querySelector('.Commande_paiement_texte'); // Sélection par la classe

    console.log('Le script est bien chargé et exécuté');

    h3Element.addEventListener('click', () => {
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

/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage texte 4   //////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const h3Element = document.getElementById('Formalités'); // Sélection par ID
    const pElement = document.querySelector('.Formalités_texte'); // Sélection par la classe

    console.log('Le script est bien chargé et exécuté');

    h3Element.addEventListener('click', () => {
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

/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction affichage texte 5   //////////////////
//////////////////////////////////////////////////////////////////////*/

document.addEventListener("DOMContentLoaded", function() {
    const h3Element = document.getElementById('Livraison'); // Sélection par ID
    const pElement = document.querySelector('.Livraison_texte'); // Sélection par la classe

    console.log('Le script est bien chargé et exécuté');

    h3Element.addEventListener('click', () => {
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

/*//////////////////////////////////////////////////////////////////////
/////////////-/////    Fonction tableau slide  //////////////////
//////////////////////////////////////////////////////////////////////*/

let currentPage = 0; // L'index de la page actuelle (0 = page1, 1 = page2, etc.)

// Tableau pour accéder aux pages
const pages = document.querySelectorAll('.Slide');

// Fonction pour afficher la page suivante
function showNextPage() {
    if (currentPage < pages.length - 1) {
        // Masquer la page actuelle
        pages[currentPage].classList.remove('active');
        currentPage++;
        // Afficher la nouvelle page
        pages[currentPage].classList.add('active');
    }
}

// Fonction pour afficher la page précédente
function showPreviousPage() {
    if (currentPage > 0) {
        // Masquer la page actuelle
        pages[currentPage].classList.remove('active');
        currentPage--;
        // Afficher la nouvelle page
        pages[currentPage].classList.add('active');
    }
}

// Ajouter les événements de clic sur les boutons
document.getElementById('Bt_gauche').addEventListener('click', showNextPage);
document.getElementById('Bt_droit').addEventListener('click', showPreviousPage);

pages[currentPage].classList.add('active');