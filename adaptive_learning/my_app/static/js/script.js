document.addEventListener('DOMContentLoaded', () => {
    // Particle Animation
    const particles = document.querySelectorAll('.particle');
    particles.forEach((particle, index) => {
        particle.style.animation = `float-slow ${10 + index * 2}s infinite ${index * 0.5}s`;
    });

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.5
    };

    // Observe content wrapper and modules container
    const contentObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                contentObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const contentWrapper = document.querySelector('.content-wrapper');
    if (contentWrapper) {
        contentObserver.observe(contentWrapper);
    }

    const modulesContainer = document.querySelector('.modules-container');
    if (modulesContainer) {
        contentObserver.observe(modulesContainer);
    }

    // Smooth scroll for navigation links
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

    // Parallax effect for hero section and navbar handling
    const nav = document.querySelector('nav');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        // Parallax effect
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.backgroundPositionY = currentScroll * 0.5 + 'px';
        }

        // Navbar visibility
        if (currentScroll <= 0) {
            nav.classList.remove('scrolled');
            nav.classList.remove('nav-hidden');
            return;
        }
        
        if (currentScroll > lastScroll && !nav.classList.contains('nav-hidden')) {
            nav.classList.add('nav-hidden');
        } else if (currentScroll < lastScroll && nav.classList.contains('nav-hidden')) {
            nav.classList.remove('nav-hidden');
        }
        
        if (currentScroll > 100) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });

    // Feature cards hover effect
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px)';
            const icon = card.querySelector('.feature-icon i');
            if (icon) {
                icon.style.transform = 'scale(1.2) rotate(5deg)';
            }
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            const icon = card.querySelector('.feature-icon i');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });

    // Mobile menu toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const body = document.body;

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenuBtn.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            body.classList.toggle('menu-open');
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileMenuBtn.classList.remove('active');
                mobileMenu.classList.remove('active');
                body.classList.remove('menu-open');
            }
        });
    }

    // ✅ Navbar Link Hover Animation ✅
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            const icon = link.querySelector('i');
            if (icon) {
                icon.style.transform = 'translateY(-3px)';
                icon.style.transition = 'transform 0.2s ease';
            }
        });

        link.addEventListener('mouseleave', () => {
            const icon = link.querySelector('i');
            if (icon) {
                icon.style.transform = 'translateY(0)';
            }
        });
    });

    // Animate numbers in step counter
    const stepNumbers = document.querySelectorAll('.step-number');
    const animateNumber = (element) => {
        const number = parseInt(element.textContent);
        let current = 0;
        const increment = number / 30;
        const timer = setInterval(() => {
            current += increment;
            if (current >= number) {
                element.textContent = number;
                clearInterval(timer);
            } else {
                element.textContent = Math.ceil(current);
            }
        }, 30);
    };

    const numberObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateNumber(entry.target);
                numberObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    stepNumbers.forEach(number => numberObserver.observe(number));

    // Typewriter effect
    const text = document.querySelector('.typewriter');
    if (text) {
        const content = text.textContent;
        text.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < content.length) {
                text.textContent += content.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        
        // Start typewriter effect after a short delay
        setTimeout(typeWriter, 500);
    }

    // Flip card functionality
    featureCards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('flipped');
        });
    });
});