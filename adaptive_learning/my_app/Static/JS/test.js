document.addEventListener("DOMContentLoaded", function() {
    const progressBar = document.getElementById("progress");
    const form = document.getElementById("test-form");
    const feedbackDiv = document.getElementById("feedback");

    // Update progress bar as user selects answers
    let totalQuestions = document.querySelectorAll(".question-card").length;
    let answeredQuestions = 0;

    document.querySelectorAll("input[type='radio']").forEach(radio => {
        radio.addEventListener("change", function() {
            answeredQuestions++;
            let progress = (answeredQuestions / totalQuestions) * 100;
            progressBar.style.width = progress + "%";

            if (answeredQuestions === totalQuestions) {
                showMotivationalMessage("You're doing great! Keep it up!");
            }
        });
    });

    // Show motivational message when the user completes the test
    form.addEventListener("submit", function(e) {
        e.preventDefault();
        showMotivationalMessage("Test submitted! Well done!");
    });

    function showMotivationalMessage(message) {
        feedbackDiv.innerHTML = `<div class="motivational-message">${message}</div>`;
    }
});
