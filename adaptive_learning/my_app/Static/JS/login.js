document.addEventListener('DOMContentLoaded', () => {
    // Scroll to login section on load
    document.querySelector('.login-section').scrollIntoView({ behavior: 'smooth' });

    // Form Validation
    document.querySelector('.submit-btn').addEventListener('click', function (event) {
        let username = document.querySelector('input[name="username"]');
        let password = document.querySelector('input[name="password"]');

        clearErrors();

        if (!username.value || !password.value) {
            event.preventDefault();

            if (!username.value) showError(username, 'Please enter your username.');
            if (!password.value) showError(password, 'Please enter your password.');
        }
    });

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

    // Button Hover Effects
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.transition = 'all 0.3s ease';
    });
    submitBtn.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
    });

    // Password Toggle Functionality (Same icon for both states)
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
