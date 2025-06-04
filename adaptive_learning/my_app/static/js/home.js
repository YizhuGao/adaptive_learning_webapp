document.addEventListener("DOMContentLoaded", () => {
    const welcomeText = document.querySelector(".welcome-text");

    function updateGreeting() {
        const hour = new Date().getHours();
        let greeting = "Hello";
        if (hour < 12) greeting = "Good Morning";
        else if (hour < 18) greeting = "Good Afternoon";
        else greeting = "Good Evening";

        const name = welcomeText.textContent.split(",")[1]?.trim() || "";
        welcomeText.textContent = `${greeting}, ${name}`;
    }

    updateGreeting();
    setInterval(updateGreeting, 60000); // Update every minute

    // Initialize particles
    initParticles();

    // Initialize navbar scroll behavior
    initNavbar();

    // Initialize mobile menu
    initMobileMenu();

    // Initialize stats animation
    initStatsAnimation();
});

// Particle animation
function initParticles() {
    const particles = document.querySelectorAll('.particle');
    particles.forEach((particle, index) => {
        // Random initial position
        const x = Math.random() * window.innerWidth;
        const y = Math.random() * window.innerHeight;
        particle.style.left = `${x}px`;
        particle.style.top = `${y}px`;

        // Random animation delay
        particle.style.animation = `float-slow 8s infinite ${index * 0.5}s`;
    });
}

// Navbar scroll behavior
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add/remove scrolled class
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Hide/show navbar based on scroll direction
        if (currentScroll > lastScroll && currentScroll > 500) {
            navbar.classList.add('nav-hidden');
        } else {
            navbar.classList.remove('nav-hidden');
        }

        lastScroll = currentScroll;
    });
}

// Mobile menu functionality
function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const menuBars = document.querySelectorAll('.mobile-menu-btn span');
    let isMenuOpen = false;

    menuBtn.addEventListener('click', () => {
        isMenuOpen = !isMenuOpen;
        
        // Toggle menu visibility
        mobileMenu.classList.toggle('active');

        // Animate menu bars
        if (isMenuOpen) {
            menuBars[0].style.transform = 'rotate(45deg) translate(6px, 6px)';
            menuBars[1].style.opacity = '0';
            menuBars[2].style.transform = 'rotate(-45deg) translate(6px, -6px)';
        } else {
            menuBars[0].style.transform = 'none';
            menuBars[1].style.opacity = '1';
            menuBars[2].style.transform = 'none';
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (isMenuOpen && !e.target.closest('.mobile-menu') && !e.target.closest('.mobile-menu-btn')) {
            isMenuOpen = false;
            mobileMenu.classList.remove('active');
            menuBars.forEach(bar => bar.style = '');
        }
    });
}

// Stats animation
function initStatsAnimation() {
    const stats = document.querySelectorAll('.stat-number');
    
    // Animate stats when they come into view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.textContent);
                animateNumber(entry.target, target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    stats.forEach(stat => observer.observe(stat));
}

// Number animation helper
function animateNumber(element, target) {
    let current = 0;
    const increment = target / 50; // Divide animation into 50 steps
    const duration = 1500; // Animation duration in milliseconds
    const stepTime = duration / 50;

    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.round(current);
        }
    }, stepTime);
}

// Feature card hover effects
document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        const icon = card.querySelector('.feature-icon i');
        icon.style.transform = 'scale(1.2) rotate(10deg)';
    });

    card.addEventListener('mouseleave', () => {
        const icon = card.querySelector('.feature-icon i');
        icon.style.transform = 'scale(1) rotate(0)';
    });
});

// Activity card hover effects
document.querySelectorAll('.activity-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        const icon = card.querySelector('.activity-icon');
        icon.style.transform = 'scale(1.1)';
    });

    card.addEventListener('mouseleave', () => {
        const icon = card.querySelector('.activity-icon');
        icon.style.transform = 'scale(1)';
    });
});
