document.addEventListener("DOMContentLoaded", function() {
    // Select all disabled input fields
    const disabledFields = document.querySelectorAll('input:disabled, select:disabled');

    // Add an event listener to each disabled field
    disabledFields.forEach(field => {
        field.addEventListener("focus", function(event) {
            // Display a generic message for non-editable fields
            showMessage("Sorry, you cannot edit this field.");
        });
    });

    // Function to display the message
    function showMessage(message) {
        const messageContainer = document.createElement("div");
        messageContainer.classList.add("message");
        messageContainer.textContent = message;

        // Add the message container to the body or any specific location on the page
        document.body.appendChild(messageContainer);

        // Automatically remove the message after 3 seconds
        setTimeout(() => {
            messageContainer.remove();
        }, 3000);
    }

    // Show/Hide Password functionality
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm_password");

    // Create eye icons for password fields
    const passwordEyeIcon = document.createElement("span");
    passwordEyeIcon.classList.add("eye-icon");
    passwordEyeIcon.innerHTML = "👁️";  // You can replace it with any icon or use an icon font

    const confirmPasswordEyeIcon = document.createElement("span");
    confirmPasswordEyeIcon.classList.add("eye-icon");
    confirmPasswordEyeIcon.innerHTML = "👁️"; // Replace with icon or use font icons

    // Append the eye icons to the password fields
    const passwordContainer = document.createElement("div");
    passwordContainer.classList.add("password-container");
    passwordInput.parentNode.appendChild(passwordContainer);
    passwordContainer.appendChild(passwordInput);
    passwordContainer.appendChild(passwordEyeIcon);

    const confirmPasswordContainer = document.createElement("div");
    confirmPasswordContainer.classList.add("password-container");
    confirmPasswordInput.parentNode.appendChild(confirmPasswordContainer);
    confirmPasswordContainer.appendChild(confirmPasswordInput);
    confirmPasswordContainer.appendChild(confirmPasswordEyeIcon);

    // Add event listeners to toggle password visibility
    passwordEyeIcon.addEventListener("click", function() {
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            passwordEyeIcon.style.color = "#9e1b32"; // Change color on visibility toggle
        } else {
            passwordInput.type = "password";
            passwordEyeIcon.style.color = "#555"; // Reset color
        }
    });

    confirmPasswordEyeIcon.addEventListener("click", function() {
        if (confirmPasswordInput.type === "password") {
            confirmPasswordInput.type = "text";
            confirmPasswordEyeIcon.style.color = "#9e1b32"; // Change color on visibility toggle
        } else {
            confirmPasswordInput.type = "password";
            confirmPasswordEyeIcon.style.color = "#555"; // Reset color
        }
    });
});
