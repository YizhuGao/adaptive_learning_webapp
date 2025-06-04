document.addEventListener("DOMContentLoaded", function() {
    // Mobile Menu Functionality
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const body = document.body;

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!mobileMenuBtn.contains(event.target) && !mobileMenu.contains(event.target)) {
                mobileMenu.classList.remove('active');
                body.style.overflow = '';
            }
        });
    }

    // Password Toggle Functionality
    const passwordToggles = [
        { input: document.getElementById('password'), icon: document.getElementById('togglePassword') },
        { input: document.getElementById('confirm_password'), icon: document.getElementById('toggleConfirmPassword') }
    ];

    passwordToggles.forEach(({ input, icon }) => {
        if (input && icon) {
            icon.addEventListener('click', () => {
                const type = input.type === 'password' ? 'text' : 'password';
                input.type = type;
                icon.querySelector('i').className = `fas fa-eye${type === 'password' ? '' : '-slash'}`;
            });
        }
    });

    // Form Validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const password = document.getElementById('password');
            const confirmPassword = document.getElementById('confirm_password');

            if (password.value || confirmPassword.value) {
                if (password.value !== confirmPassword.value) {
                    event.preventDefault();
                    showMessage('Passwords do not match!');
                    return;
                }

                if (password.value.length < 8) {
                    event.preventDefault();
                    showMessage('Password must be at least 8 characters long!');
                    return;
                }
            }
        });
    }

    // Message Display
    function showMessage(text, type = 'error') {
        const existingMessage = document.querySelector('.message');
        if (existingMessage) {
            existingMessage.remove();
        }

        const message = document.createElement('div');
        message.className = 'message';
        message.textContent = text;
        
        if (type === 'success') {
            message.style.backgroundColor = '#38a169';
        }

        document.body.appendChild(message);

        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 3000);
    }

    // Input Animations
    const inputs = document.querySelectorAll('input:not([disabled]), select');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', () => {
            input.parentElement.classList.remove('focused');
        });
    });

    // Prevent form submission on disabled fields
    const disabledFields = document.querySelectorAll('input:disabled, select:disabled');
    disabledFields.forEach(field => {
        field.addEventListener('click', () => {
            showMessage('This field cannot be edited');
        });
    });
});
