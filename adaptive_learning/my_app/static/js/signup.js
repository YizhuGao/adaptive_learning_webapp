// signup.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize particles
    initParticles();

    // Initialize navbar scroll behavior
    initNavbar();

    // Initialize form validation
    initFormValidation();
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

// Form validation
function initFormValidation() {
    const form = document.querySelector('form');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirm_password');
    const submitBtn = document.querySelector('.submit-btn');

    // Email validation
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Password validation
    function isValidPassword(password) {
        // At least 8 characters, 1 uppercase, 1 lowercase, 1 number
        const re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
        return re.test(password);
    }

    // Show error message
    function showError(input, message) {
        const formGroup = input.closest('.form-group');
        let errorDiv = formGroup.querySelector('.error-message');
        
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
            formGroup.appendChild(errorDiv);
        } else {
            errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
        }
        
        input.classList.add('error');
    }

    // Remove error message
    function removeError(input) {
        const formGroup = input.closest('.form-group');
        const errorDiv = formGroup.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
        input.classList.remove('error');
    }

    // Real-time email validation
    emailInput.addEventListener('input', () => {
        if (!isValidEmail(emailInput.value)) {
            showError(emailInput, 'Please enter a valid email address');
        } else {
            removeError(emailInput);
        }
    });

    // Real-time password validation
    passwordInput.addEventListener('input', () => {
        if (!isValidPassword(passwordInput.value)) {
            showError(passwordInput, 'Password must be at least 8 characters with 1 uppercase, 1 lowercase, and 1 number');
        } else {
            removeError(passwordInput);
        }
    });

    // Real-time confirm password validation
    confirmPasswordInput.addEventListener('input', () => {
        if (confirmPasswordInput.value !== passwordInput.value) {
            showError(confirmPasswordInput, 'Passwords do not match');
        } else {
            removeError(confirmPasswordInput);
        }
    });

    // Form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        let isValid = true;

        // Validate all required fields
        form.querySelectorAll('input[required], select[required]').forEach(input => {
            if (!input.value.trim()) {
                showError(input, 'This field is required');
                isValid = false;
            }
        });

        // Validate email
        if (!isValidEmail(emailInput.value)) {
            showError(emailInput, 'Please enter a valid email address');
            isValid = false;
        }

        // Validate password
        if (!isValidPassword(passwordInput.value)) {
            showError(passwordInput, 'Password must be at least 8 characters with 1 uppercase, 1 lowercase, and 1 number');
            isValid = false;
        }

        // Validate confirm password
        if (confirmPasswordInput.value !== passwordInput.value) {
            showError(confirmPasswordInput, 'Passwords do not match');
            isValid = false;
        }

        if (isValid) {
            // Show loading state
            submitBtn.classList.add('loading');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Creating Account...';
            submitBtn.disabled = true;

            try {
                // Submit the form
                form.submit();
            } catch (error) {
                // Handle submission error
                submitBtn.classList.remove('loading');
                submitBtn.innerHTML = '<span>Create Account</span><i class="fas fa-arrow-right"></i>';
                submitBtn.disabled = false;
                
                // Show error message at the top of the form
                const errorMessages = document.querySelector('.error-messages') || document.createElement('div');
                errorMessages.className = 'error-messages';
                errorMessages.innerHTML = `
                    <div class="error-message">
                        <i class="fas fa-exclamation-circle"></i>
                        An error occurred. Please try again.
                    </div>
                `;
                form.insertBefore(errorMessages, form.firstChild);
            }
        }
    });
}

window.addEventListener('load', () => {
    document.querySelector('.login-section').scrollIntoView({ behavior: 'smooth' });

    // Add eye toggle icons
    const passwordFields = document.querySelectorAll('input[type="password"]');

    passwordFields.forEach(input => {
        const eyeIcon = document.createElement('span');
        eyeIcon.classList.add('toggle-password');
        eyeIcon.innerHTML = '👁️';

        input.parentElement.style.position = 'relative';
        input.parentElement.appendChild(eyeIcon);

        eyeIcon.addEventListener('click', () => {
            const isHidden = input.type === 'password';
            input.type = isHidden ? 'text' : 'password';
            eyeIcon.style.color = isHidden ? '#9e1b32' : '#555';
        });
    });
});

// Form Validation
document.querySelector('.submit-btn').addEventListener('click', function (event) {
    const username = document.querySelector('input[name="username"]');
    const email = document.querySelector('input[name="email"]');
    const password = document.querySelector('input[name="password"]');
    const confirmPassword = document.querySelector('input[name="confirm_password"]');

    clearErrors();

    let hasError = false;

    if (!username.value) {
        showError(username, 'Please enter your username.');
        hasError = true;
    }

    if (!email.value) {
        showError(email, 'Please enter your email.');
        hasError = true;
    }

    if (!password.value) {
        showError(password, 'Please enter your password.');
        hasError = true;
    }

    if (!confirmPassword.value) {
        showError(confirmPassword, 'Please confirm your password.');
        hasError = true;
    }

    if (password.value && confirmPassword.value && password.value !== confirmPassword.value) {
        showError(confirmPassword, 'Passwords do not match.');
        hasError = true;
    }

    if (hasError) event.preventDefault();
});

function showError(input, message) {
    input.classList.add('error');
    const errorMessage = document.createElement('p');
    errorMessage.classList.add('error-message');
    errorMessage.textContent = message;
    input.parentElement.appendChild(errorMessage);
}

function clearErrors() {
    document.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
    document.querySelectorAll('.error-message').forEach(el => el.remove());
}
