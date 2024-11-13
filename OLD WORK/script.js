document.addEventListener('DOMContentLoaded', () => {
    // Scroll Animation
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe content wrapper
    const contentWrapper = document.querySelector('.content-wrapper');
    if (contentWrapper) {
        observer.observe(contentWrapper);
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

    // Scroll-based animations for nav
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('nav');
        const currentScroll = window.pageYOffset;

        if (currentScroll <= 0) {
            nav.classList.remove('scroll-up');
            return;
        }

        if (currentScroll > lastScroll && !nav.classList.contains('scroll-down')) {
            nav.classList.remove('scroll-up');
            nav.classList.add('scroll-down');
        } else if (currentScroll < lastScroll && nav.classList.contains('scroll-down')) {
            nav.classList.remove('scroll-down');
            nav.classList.add('scroll-up');
        }
        lastScroll = currentScroll;
    });

    const modulesContainer = document.querySelector('.modules-container');
    if (modulesContainer) {
        observer.observe(modulesContainer);
    }

    // Hover effect for module cards
    const moduleCards = document.querySelectorAll('.module-card');
    moduleCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });

    // Module Detail View Functionality
    const moduleDetail = document.querySelector('.module-detail');
    const closeButtons = document.querySelectorAll('.close-module');
    const moduleContents = document.querySelectorAll('.module-content');

    // Function to open module detail
    function openModuleDetail(moduleType) {
        console.log('Opening module:', moduleType); // Debugging log
        moduleDetail.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling

        // Hide all module contents first
        moduleContents.forEach(content => {
            content.classList.remove('active');
        });

        // Show the selected module content
        const selectedContent = document.querySelector(`[data-module="${moduleType}"]`);
        if (selectedContent) {
            selectedContent.classList.add('active');
        } else {
            console.log('Module not found:', moduleType); // Debugging log
            // Optionally, show a fallback message or error
        }
    }

    // Function to close module detail
    function closeModuleDetail() {
        moduleDetail.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling

        moduleContents.forEach(content => {
            content.classList.remove('active');
        });
    }

    // Add click listeners to module cards
    moduleCards.forEach(card => {
        card.addEventListener('click', () => {
            const moduleType = card.getAttribute('data-module');
            console.log('Module card clicked:', moduleType); // Debugging log
            openModuleDetail(moduleType);
        });
    });

    // Add click listeners to close buttons
    closeButtons.forEach(button => {
        button.addEventListener('click', closeModuleDetail);
    });

    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModuleDetail();
        }
    });

    // Close on click outside
    moduleDetail.addEventListener('click', (e) => {
        if (e.target === moduleDetail) {
            closeModuleDetail();
        }
    });

    const modulesButton = document.getElementById('modulesBtn');
    const modulesSection = document.getElementById('modules');

    // Scroll to modules section only when the button is clicked
    if (modulesButton && modulesSection) {
        modulesButton.addEventListener('click', () => {
            modulesSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    }
});
