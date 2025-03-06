document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const firstName = document.querySelector('input[name="first_name"]');
    const lastName = document.querySelector('input[name="last_name"]');
    const submitButton = document.querySelector('.submit-btn');

    // Smooth scroll to profile update section on page load
    document.querySelector('.login-section').scrollIntoView({ behavior: 'smooth' });

    // Password Validation
    function validatePassword() {
        if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity("Passwords do not match!");
            confirmPassword.style.border = "2px solid red";
        } else {
            confirmPassword.setCustomValidity("");
            confirmPassword.style.border = "2px solid green";
        }
    }

    password.addEventListener("input", validatePassword);
    confirmPassword.addEventListener("input", validatePassword);

    // Form Validation
    form.addEventListener("submit", function(event) {
        clearErrors();
        let hasError = false;

        if (!firstName.value.trim()) {
            showError(firstName, "Please enter your first name.");
            hasError = true;
        }
        if (!lastName.value.trim()) {
            showError(lastName, "Please enter your last name.");
            hasError = true;
        }
        if (!password.value.trim()) {
            showError(password, "Please enter a password.");
            hasError = true;
        }
        if (!confirmPassword.value.trim()) {
            showError(confirmPassword, "Please confirm your password.");
            hasError = true;
        }
        if (password.value !== confirmPassword.value) {
            showError(confirmPassword, "Passwords do not match.");
            hasError = true;
        }

        if (hasError) {
            event.preventDefault();
        }
    });

    // Show Error Function
    function showError(input, message) {
        input.classList.add("error");
        let errorMessage = document.createElement("p");
        errorMessage.classList.add("error-message");
        errorMessage.textContent = message;
        input.parentElement.appendChild(errorMessage);
    }

    // Clear Errors Function
    function clearErrors() {
        document.querySelectorAll(".error-message").forEach(msg => msg.remove());
        document.querySelectorAll(".error").forEach(input => input.classList.remove("error"));
    }

    // Button Hover Effects
    submitButton.addEventListener("mouseenter", function() {
        this.style.transform = "scale(1.05)";
    });

    submitButton.addEventListener("mouseleave", function() {
        this.style.transform = "scale(1)";
    });
});
