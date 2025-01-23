// Sélectionne les éléments HTML
const h3Element = document.getElementById('controle_rapport'); // Sélectionne le h3 par son ID
const pElement = document.querySelector('.Procédure_texte'); // Sélectionne le p avec la classe

// Ajoute un événement au clic sur le h3
h3Element.addEventListener('click', () => {
    // Si le p est caché, on l'affiche, sinon on le cache
    if (pElement.style.display === 'none') {
        pElement.style.display = 'block'; // Affiche le texte
    } else {
        pElement.style.display = 'none'; // Cache le texte
    }
});