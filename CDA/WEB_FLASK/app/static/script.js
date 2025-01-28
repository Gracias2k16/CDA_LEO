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

document.addEventListener("DOMContentLoaded", () => {
    const pages = document.querySelectorAll('.Slide'); // Toutes les pages
    let currentPage = 0; // Page actuelle (commence à 0)

    // Vérifier si des pages existent
    if (pages.length === 0) {
        console.error("Aucune page trouvée !");
        return;
    }

    // Masquer toutes les pages sauf la première
    pages.forEach((page, index) => {
        page.style.display = index === currentPage ? 'block' : 'none';
    });

    // Fonction pour afficher la page suivante
    function showNextPage() {
        if (currentPage < pages.length - 1) {
            pages[currentPage].classList.remove('active');
            pages[currentPage].style.display = 'none'; // Masquer la page actuelle
            currentPage++;
            pages[currentPage].classList.add('active');
            pages[currentPage].style.display = 'block'; // Afficher la nouvelle page
        } else {
            console.warn("Fin des pages atteinte.");
        }
    }

    // Fonction pour afficher la page précédente
    function showPreviousPage() {
        if (currentPage > 0) {
            pages[currentPage].classList.remove('active');
            pages[currentPage].style.display = 'none'; // Masquer la page actuelle
            currentPage--;
            pages[currentPage].classList.add('active');
            pages[currentPage].style.display = 'block'; // Afficher la nouvelle page
        } else {
            console.warn("Début des pages atteint.");
        }
    }

    // Ajouter les événements de clic sur les boutons
    const leftButton = document.querySelector('.Bt_gauche'); // Bouton gauche
    const rightButton = document.querySelector('.Bt_droit'); // Bouton droit

    if (leftButton && rightButton) {
        leftButton.addEventListener('click', showPreviousPage);
        rightButton.addEventListener('click', showNextPage);
    } else {
        console.error("Boutons non trouvés !");
    }

    // Afficher uniquement la première page au démarrage
    pages[currentPage].classList.add('active');
    pages[currentPage].style.display = 'block';
});