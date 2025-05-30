// signup.js

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
