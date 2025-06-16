document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu functionality
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            document.body.classList.toggle('menu-active');
        });
    }

    // Module card flip functionality
    const moduleCards = document.querySelectorAll('.module-card');
    let flippedCard = null;

    moduleCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Don't flip if clicking the CTA button
            if (e.target.closest('.cta-button')) {
                return;
            }

            // If this card is already flipped, unflip it
            if (this.classList.contains('flipped')) {
                this.classList.remove('flipped');
                flippedCard = null;
                return;
            }

            // If another card is flipped, unflip it first
            if (flippedCard) {
                flippedCard.classList.remove('flipped');
            }

            // Flip this card
            this.classList.add('flipped');
            flippedCard = this;
        });
    });

    // Close flipped card when clicking outside
    document.addEventListener('click', function(e) {
        if (flippedCard && !e.target.closest('.module-card')) {
            flippedCard.classList.remove('flipped');
            flippedCard = null;
        }
    });

    // Highlight active navbar link
    const navLinks = document.querySelectorAll('.navbar .right a');
    navLinks.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });
});
