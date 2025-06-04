document.addEventListener('DOMContentLoaded', () => {
    // Scroll to login section on load
    document.querySelector('.login-section').scrollIntoView({ behavior: 'smooth' });

    // Particle Animation
    const particles = document.querySelectorAll('.particle');
    particles.forEach((particle, index) => {
        particle.style.animation = `float-slow ${10 + index * 2}s infinite ${index * 0.5}s`;
        
        // Random initial position
        particle.style.left = `${Math.random() * 100}vw`;
        particle.style.top = `${Math.random() * 100}vh`;
    });

    // Form Animations and Validation
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input');
    const submitBtn = form.querySelector('.submit-btn');

    // Button Hover Effects
    if (submitBtn) {
        submitBtn.addEventListener('mouseenter', function () {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'all 0.3s ease';
        });
        submitBtn.addEventListener('mouseleave', function () {
            this.style.transform = 'scale(1)';
        });
    }

    // Input focus effects
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', () => {
            if (!input.value) {
                input.parentElement.classList.remove('focused');
            }
        });

        // Add animation if input has value
        if (input.value) {
            input.parentElement.classList.add('focused');
        }
    });

    // Form submission handling
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Add loading state
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;
        
        try {
            const formData = new FormData(form);
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            });

            if (response.redirected) {
                window.location.href = response.url;
            } else {
                const data = await response.text();
                document.documentElement.innerHTML = data;
                // Reinitialize AOS after page update
                AOS.refresh();
            }
        } catch (error) {
            console.error('Login error:', error);
            // Show error message
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.innerHTML = `
                <i class="fas fa-exclamation-circle"></i>
                An error occurred. Please try again.
            `;
            form.insertBefore(errorDiv, submitBtn);
        } finally {
            // Remove loading state
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
        }
    });

    // Navbar scroll effect
    let lastScroll = 0;
    const nav = document.querySelector('nav');

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
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

    // Logo spin animation
    const logo = document.querySelector('.fa-atom');
    if (logo) {
        logo.addEventListener('mouseenter', () => {
            logo.style.transform = 'rotate(360deg)';
        });
        
        logo.addEventListener('mouseleave', () => {
            logo.style.transform = 'rotate(0deg)';
        });
    }

    // Form Validation
    if (submitBtn) {
        submitBtn.addEventListener('click', function (event) {
            let username = document.querySelector('input[name="username"]');
            let password = document.querySelector('input[name="password"]');

            clearErrors();

            if (!username.value || !password.value) {
                event.preventDefault();

                if (!username.value) showError(username, 'Please enter your username.');
                if (!password.value) showError(password, 'Please enter your password.');
            }
        });
    }

    function showError(input, message) {
        input.classList.add('error');
        let errorMessage = document.createElement('p');
        errorMessage.classList.add('error-message');
        errorMessage.textContent = message;
        input.parentElement.appendChild(errorMessage);
    }

    function clearErrors() {
        document.querySelectorAll('.error-message').forEach(msg => msg.remove());
        document.querySelectorAll('.error').forEach(input => input.classList.remove('error'));
    }

    // Password Toggle Functionality
    const passwordInput = document.querySelector('input[name="password"]');
    const confirmPasswordInput = document.querySelector('input[name="confirm_password"]');

    function createToggleIcon(inputField) {
        const container = document.createElement('div');
        container.classList.add('password-container');

        const eyeIcon = document.createElement('span');
        eyeIcon.classList.add('eye-icon');
        eyeIcon.innerHTML = '👁️'; // Same icon for both states

        inputField.parentNode.insertBefore(container, inputField);
        container.appendChild(inputField);
        container.appendChild(eyeIcon);

        eyeIcon.addEventListener('click', () => {
            const isPassword = inputField.type === 'password';
            inputField.type = isPassword ? 'text' : 'password';
            eyeIcon.style.color = isPassword ? '#9e1b32' : '#555'; // Optional color toggle
        });
    }

    if (passwordInput) createToggleIcon(passwordInput);
    if (confirmPasswordInput) createToggleIcon(confirmPasswordInput);

    // Responsive Navbar Padding
    window.addEventListener('resize', () => {
        const navbar = document.querySelector('.login-nav');
        const windowWidth = window.innerWidth;
        if (navbar) {
            navbar.style.padding = windowWidth <= 768 ? '1rem' : '1rem 3rem';
        }
    });
});
