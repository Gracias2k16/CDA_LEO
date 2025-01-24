document.addEventListener("DOMContentLoaded", function() {
    const h3Element = document.getElementById('Recherche_véhicule'); // Sélectionne le h3 par son ID
    const pElement = document.querySelector('.Recherche_véhicule_texte'); // Sélectionne le p avec la classe
    const ulElement = document.getElementById('Dynamic_list');

    console.log('Le script est bien chargé et exécuté');

    h3Element.addEventListener('click', () => {
        console.log('Clic sur le h3 détecté');
        
        if (pElement.style.display === 'none' || pElement.style.display === '') {
            pElement.style.display = 'block'; // Affiche le texte
            ulElement.style.display = 'block'; // Affiche la liste
            console.log('Le texte a été affiché');

        } else {
            pElement.style.display = 'none'; // Cache le texte
            ulElement.style.display = 'none'; // Cache la Liste
            console.log('Le texte a été caché');
        }
    });
});
