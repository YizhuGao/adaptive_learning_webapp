document.addEventListener("DOMContentLoaded", () => {
    // Initialize AOS
    AOS.init({
        once: true,
        duration: 1000,
        offset: 100
    });

    // Initialize particles with experimental theme
    initExperimentalParticles();

    // Initialize navbar scroll behavior
    initNavbar();

    // Initialize mobile menu
    initMobileMenu();

    // Initialize feature card animations
    initFeatureCards();
});

// Experimental particle animation
function initExperimentalParticles() {
    const particles = document.querySelectorAll('.particle');
    particles.forEach((particle, index) => {
        // Random initial position
        const x = Math.random() * window.innerWidth;
        const y = Math.random() * window.innerHeight;
        particle.style.left = `${x}px`;
        particle.style.top = `${y}px`;

        // Random animation delay and duration
        const duration = 8 + Math.random() * 4; // Random duration between 8-12s
        const delay = index * 0.5;
        particle.style.animation = `float-slow ${duration}s infinite ${delay}s`;

        // Add experimental theme class
        particle.classList.add('experiment-particle');
    });
}

// Feature card animations
function initFeatureCards() {
    const cards = document.querySelectorAll('.feature-card');
    
    cards.forEach(card => {
        // Add hover effect
        card.addEventListener('mouseenter', () => {
            const icon = card.querySelector('.feature-icon i');
            icon.style.transform = 'scale(1.2) rotate(10deg)';
            
            // Add floating animation
            card.style.animation = 'experiment-float 2s ease-in-out infinite';
        });

        card.addEventListener('mouseleave', () => {
            const icon = card.querySelector('.feature-icon i');
            icon.style.transform = 'scale(1) rotate(0)';
            
            // Remove floating animation
            card.style.animation = 'none';
        });
    });
}

// CTA button hover effect
const ctaButton = document.querySelector('.cta-button');
if (ctaButton) {
    ctaButton.addEventListener('mouseenter', () => {
        const glow = ctaButton.querySelector('.button-glow');
        glow.style.opacity = '1';
        glow.style.transform = 'scale(1.5)';
    });

    ctaButton.addEventListener('mouseleave', () => {
        const glow = ctaButton.querySelector('.button-glow');
        glow.style.opacity = '0';
        glow.style.transform = 'scale(1)';
    });
}

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Mobile Menu Toggle
document.querySelector('.mobile-menu-btn').addEventListener('click', function() {
    document.querySelector('.mobile-menu').classList.toggle('active');
});

// Navbar Scroll Effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll <= 0) {
        navbar.classList.remove('scrolled');
        return;
    }
    
    if (currentScroll > lastScroll && !navbar.classList.contains('nav-hidden')) {
        // Scrolling down
        navbar.classList.add('nav-hidden');
    } else if (currentScroll < lastScroll && navbar.classList.contains('nav-hidden')) {
        // Scrolling up
        navbar.classList.remove('nav-hidden');
    }
    
    navbar.classList.add('scrolled');
    lastScroll = currentScroll;
}); 