document.addEventListener('DOMContentLoaded', () => {
    // Handle flashcard flip effect
    const flashcards = document.querySelectorAll('.flashcard');

    flashcards.forEach(card => {
        card.addEventListener('click', () => {
            flashcards.forEach(item => {
                if (item !== card) item.classList.remove('flip');
            });
            card.classList.toggle('flip');
        });
    });

    // Highlight active navbar link
    const navLinks = document.querySelectorAll('.navbar .right a');
    navLinks.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });
});
