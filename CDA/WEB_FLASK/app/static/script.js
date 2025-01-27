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

