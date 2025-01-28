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
    const pages = document.querySelectorAll('.Slide'); // Toutes les slides
    let currentPage = 0; // Page actuelle (commence à 0)

    // Initialisation : afficher uniquement la première page
    function updateSlides() {
        pages.forEach((page, index) => {
            page.style.display = index === currentPage ? 'block' : 'none';
        });
    }
    updateSlides();

    // Gestion des boutons dynamiquement
    function attachButtonEvents() {
        const currentSlide = pages[currentPage];

        // Sélection des boutons dans la slide active
        const prevButton = currentSlide.querySelector('.Bt_gauche');
        const nextButton = currentSlide.querySelector('.Bt_droit');

        // Ajouter les gestionnaires d'événements
        if (prevButton) {
            prevButton.addEventListener('click', () => {
                if (currentPage > 0) {
                    currentPage--;
                    updateSlides();
                    attachButtonEvents(); // Réattacher les événements pour la nouvelle page
                }
            });
        }

        if (nextButton) {
            nextButton.addEventListener('click', () => {
                if (currentPage < pages.length - 1) {
                    currentPage++;
                    updateSlides();
                    attachButtonEvents(); // Réattacher les événements pour la nouvelle page
                }
            });
        }
    }

    // Attacher les événements pour la première fois
    attachButtonEvents();
});