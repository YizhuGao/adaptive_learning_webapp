// Cache DOM elements and optimize event listeners
const DOM = {
    welcomeText: document.querySelector(".welcome-text"),
    navbar: document.querySelector('.navbar'),
    menuBtn: document.querySelector('.mobile-menu-btn'),
    mobileMenu: document.querySelector('.mobile-menu'),
    menuBars: document.querySelectorAll('.mobile-menu-btn span'),
    featureCards: document.querySelectorAll('.feature-card'),
    activityCards: document.querySelectorAll('.activity-card'),
    stats: document.querySelectorAll('.stat-number')
};

// Debounce function to limit function calls
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function to limit function calls
function throttle(func, limit) {
    let inThrottle;
    return function executedFunction(...args) {
        if (!inThrottle) {
            func(...args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

document.addEventListener("DOMContentLoaded", () => {
    // Initialize all components
    initGreeting();
    initParticles();
    initNavbar();
    initMobileMenu();
    initStatsAnimation();
    initAOS();
    initSmoothScroll();
    initFeatureCards();
});

function initGreeting() {
    function updateGreeting() {
        const hour = new Date().getHours();
        const name = DOM.welcomeText.textContent.split(",")[1]?.trim() || "";
        const greeting = hour < 12 ? "Good Morning" : 
                        hour < 18 ? "Good Afternoon" : 
                        "Good Evening";
        DOM.welcomeText.textContent = `${greeting}, ${name}`;
    }

    updateGreeting();
    // Use setInterval with a longer duration
    setInterval(updateGreeting, 300000); // Update every 5 minutes
}

function initParticles() {
    const particles = document.querySelectorAll('.particle');
    const fragment = document.createDocumentFragment();
    
    particles.forEach((particle, index) => {
        const x = Math.random() * window.innerWidth;
        const y = Math.random() * window.innerHeight;
        particle.style.cssText = `
            left: ${x}px;
            top: ${y}px;
            animation: float-slow 8s infinite ${index * 0.5}s;
        `;
        fragment.appendChild(particle);
    });
    
    document.body.appendChild(fragment);
}

function initNavbar() {
    let lastScroll = 0;
    
    const handleScroll = throttle(() => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 50) {
            DOM.navbar.classList.add('scrolled');
        } else {
            DOM.navbar.classList.remove('scrolled');
        }

        if (currentScroll > lastScroll && currentScroll > 500) {
            DOM.navbar.classList.add('nav-hidden');
        } else {
            DOM.navbar.classList.remove('nav-hidden');
        }

        lastScroll = currentScroll;
    }, 100);

    window.addEventListener('scroll', handleScroll, { passive: true });
}

function initMobileMenu() {
    let isMenuOpen = false;

    const toggleMenu = () => {
        isMenuOpen = !isMenuOpen;
        DOM.mobileMenu.classList.toggle('active');
        
        if (isMenuOpen) {
            DOM.menuBars[0].style.transform = 'rotate(45deg) translate(6px, 6px)';
            DOM.menuBars[1].style.opacity = '0';
            DOM.menuBars[2].style.transform = 'rotate(-45deg) translate(6px, -6px)';
        } else {
            DOM.menuBars[0].style.transform = '';
            DOM.menuBars[1].style.opacity = '1';
            DOM.menuBars[2].style.transform = '';
        }
    };

    DOM.menuBtn.addEventListener('click', toggleMenu);

    // Use event delegation for document click
    document.addEventListener('click', (e) => {
        if (isMenuOpen && !e.target.closest('.mobile-menu') && !e.target.closest('.mobile-menu-btn')) {
            toggleMenu();
        }
    });
}

function initStatsAnimation() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.textContent);
                animateNumber(entry.target, target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5,
        rootMargin: '50px'
    });

    DOM.stats.forEach(stat => observer.observe(stat));
}

function animateNumber(element, target) {
    const duration = 1500;
    const steps = 50;
    const increment = target / steps;
    const stepTime = duration / steps;
    let current = 0;

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

function initAOS() {
    if (typeof AOS !== 'undefined') {
        AOS.init({
            once: true,
            duration: 800,
            offset: 50,
            disable: 'mobile',
            useClassNames: true,
            disableMutationObserver: false
        });
    }
}

function initSmoothScroll() {
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
}

function initFeatureCards() {
    DOM.featureCards.forEach(card => {
        const handleHover = (isEnter) => {
            requestAnimationFrame(() => {
                card.style.transform = isEnter ? 'translateY(-5px)' : 'translateY(0)';
            });
        };

        card.addEventListener('mouseenter', () => handleHover(true));
        card.addEventListener('mouseleave', () => handleHover(false));
    });
}

// Activity card hover effects with event delegation
document.addEventListener('mouseover', (e) => {
    const card = e.target.closest('.activity-card');
    if (card) {
        const icon = card.querySelector('.activity-icon');
        if (icon) {
            requestAnimationFrame(() => {
                icon.style.transform = 'scale(1.1)';
            });
        }
    }
});

document.addEventListener('mouseout', (e) => {
    const card = e.target.closest('.activity-card');
    if (card) {
        const icon = card.querySelector('.activity-icon');
        if (icon) {
            requestAnimationFrame(() => {
                icon.style.transform = 'scale(1)';
            });
        }
    }
});
