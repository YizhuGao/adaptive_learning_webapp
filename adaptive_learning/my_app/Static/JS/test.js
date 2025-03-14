document.addEventListener("DOMContentLoaded", () => {
    const progressBar = document.getElementById("progress");
    const form = document.querySelector("form");
    const feedbackDiv = document.getElementById("feedback");

    const totalQuestions = document.querySelectorAll(".question-card").length;
    let answeredQuestions = new Set();

    // Track and update progress based on unique answers
    document.querySelectorAll("input[type='radio']").forEach(radio => {
        radio.addEventListener("change", (event) => {
            const questionName = event.target.name;

            if (event.target.checked) {
                answeredQuestions.add(questionName); // Add only unique answered question
            }

            // Update progress bar only based on uniquely answered questions
            updateProgressBar();
        });
    });

    // Function to update the progress bar
    function updateProgressBar() {
        const progress = (answeredQuestions.size / totalQuestions) * 100;
        progressBar.style.width = `${progress}%`;

        if (answeredQuestions.size === totalQuestions) {
            showMotivationalMessage("You're doing great! Keep going!");
        }
    }

    // Handle form submission
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        if (answeredQuestions.size < totalQuestions) {
            showMotivationalMessage("Please answer all questions before submitting.");
            return;
        }

        showMotivationalMessage("Test submitted! Well done!");

        // Add slight delay before form submission for better UX
        setTimeout(() => {
            form.submit();
        }, 1000);
    });

    // Function to display motivational message
    function showMotivationalMessage(message) {
        feedbackDiv.innerHTML = `<div class="motivational-message">${message}</div>`;
        feedbackDiv.style.opacity = "1";

        // Fade out message after 3 seconds
        setTimeout(() => {
            feedbackDiv.style.opacity = "0";
        }, 3000);
    }

    // Ensure progress bar is reset on page reload
    window.addEventListener("beforeunload", () => {
        progressBar.style.width = "0%";
        answeredQuestions.clear();
    });

    // Adjust Navbar padding on resize for responsiveness
    window.addEventListener('resize', () => {
        const navbar = document.querySelector('.navbar');
        const windowWidth = window.innerWidth;
        if (windowWidth <= 768) {
            navbar.style.padding = '12px 20px';
        } else {
            navbar.style.padding = '15px 40px';
        }
    });

    // Scroll to top on page load for better UX
    window.scrollTo(0, 0);
});
