// Smooth Scroll to Login Section when page loads
window.addEventListener('load', () => {
    document.querySelector('.login-section').scrollIntoView({ behavior: 'smooth' });
});

// Form Validation: Check if fields are empty and highlight with animations
document.querySelector('.submit-btn').addEventListener('click', function (event) {
    let username = document.querySelector('input[name="username"]');
    let password = document.querySelector('input[name="password"]');
    
    // Clear previous error messages
    clearErrors();

    // Check if fields are empty
    if (!username.value || !password.value) {
        event.preventDefault();
        
        // Apply error styles and show messages
        if (!username.value) {
            showError(username, 'Please enter your username.');
        }
        if (!password.value) {
            showError(password, 'Please enter your password.');
        }
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

// Apply smooth transition on submit button hover
document.querySelector('.submit-btn').addEventListener('mouseenter', function () {
    this.style.transform = 'scale(1.05)';
    this.style.transition = 'all 0.3s ease';
});

document.querySelector('.submit-btn').addEventListener('mouseleave', function () {
    this.style.transform = 'scale(1)';
});

// Password visibility toggle
const togglePassword = document.querySelector('#toggle-password');
const passwordInput = document.querySelector('input[name="password"]');

togglePassword.addEventListener('click', () => {
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;
    togglePassword.textContent = type === 'password' ? 'Show' : 'Hide';
});

// Adjust Navbar for Overflow
window.addEventListener('resize', () => {
    const navbar = document.querySelector('.login-nav');
    const windowWidth = window.innerWidth;
    if (windowWidth <= 768) {
        navbar.style.padding = '1rem'; // Adjust navbar padding on smaller screens
    } else {
        navbar.style.padding = '1rem 3rem'; // Reset padding for larger screens
    }
});
