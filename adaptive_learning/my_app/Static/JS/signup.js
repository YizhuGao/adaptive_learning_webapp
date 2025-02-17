// Smooth Scroll to Sign Up Section when page loads
window.addEventListener('load', () => {
    document.querySelector('.login-section').scrollIntoView({ behavior: 'smooth' });
});

// Form Validation: Check if fields are empty and highlight with animations
document.querySelector('.submit-btn').addEventListener('click', function (event) {
    let username = document.querySelector('input[name="username"]');
    let email = document.querySelector('input[name="email"]');
    let password = document.querySelector('input[name="password"]');
    let confirmPassword = document.querySelector('input[name="confirm_password"]');
    
    // Clear previous error messages
    clearErrors();

    // Check if fields are empty
    if (!username.value || !email.value || !password.value || !confirmPassword.value) {
        event.preventDefault();
        
        // Apply error styles and show messages
        if (!username.value) {
            showError(username, 'Please enter your username.');
        }
        if (!email.value) {
            showError(email, 'Please enter your email.');
        }
        if (!password.value) {
            showError(password, 'Please enter your password.');
        }
        if (!confirmPassword.value) {
            showError(confirmPassword, 'Please confirm your password.');
        }
    }

    // Password confirmation check
    if (password.value !== confirmPassword.value) {
        event.preventDefault();
        showError(confirmPassword, 'Passwords do not match.');
    }
});

// Show Error function (Highlight input and show message)
function showError(input, message) {
    input.classList.add('error');
    let errorMessage = document.createElement('p');
    errorMessage.classList.add('error-message');
    errorMessage.textContent = message;
    input.parentElement.appendChild(errorMessage);
}

// Clear Errors function
function clearErrors() {
    let errorMessages = document.querySelectorAll('.error-message');
    let errorInputs = document.querySelectorAll('.error');

    errorMessages.forEach(msg => msg.remove());
    errorInputs.forEach(input => input.classList.remove('error'));
}

// Apply smooth transition on submit button click
document.querySelector('.submit-btn').addEventListener('mouseenter', function () {
    this.style.transform = 'scale(1.05)';
    this.style.transition = 'all 0.3s ease';
});

document.querySelector('.submit-btn').addEventListener('mouseleave', function () {
    this.style.transform = 'scale(1)';
});
