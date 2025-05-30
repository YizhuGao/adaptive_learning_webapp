document.addEventListener("DOMContentLoaded", function() {
    const questions = document.querySelectorAll(".question-card");
    const nextBtn = document.getElementById("next-btn");
    const prevBtn = document.getElementById("prev-btn");
    const submitBtn = document.querySelector(".submit-btn");
    const form = document.querySelector("form");
    const progress = document.getElementById("progress");

    let currentQuestion = 0;
    let answeredQuestions = new Set();

    // Show the current question only
    function showQuestion(index) {
        questions.forEach((q, i) => {
            q.style.display = (i === index) ? "block" : "none";
        });

        prevBtn.disabled = index === 0;
        nextBtn.disabled = index === questions.length - 1;
    }

    // Update progress bar and submit button state
    function updateProgressAndSubmit() {
        const percentage = (answeredQuestions.size / questions.length) * 100;
        progress.style.width = percentage + "%";
        // progress.innerText = Math.round(percentage) + "%";

        // Enable Submit only if all questions are answered
        submitBtn.disabled = answeredQuestions.size !== questions.length;
    }

    // When a radio option is selected
    const allOptions = document.querySelectorAll('input[type="radio"]');
    allOptions.forEach(option => {
        option.addEventListener('change', function() {
            const questionCard = this.closest(".question-card");
            const questionIndex = Array.from(questions).indexOf(questionCard);

            if (questionIndex !== -1) {
                answeredQuestions.add(questionIndex);
                updateProgressAndSubmit();
            }
        });
    });

    // Navigation buttons
    nextBtn.addEventListener("click", function() {
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            showQuestion(currentQuestion);
        }
    });

    prevBtn.addEventListener("click", function() {
        if (currentQuestion > 0) {
            currentQuestion--;
            showQuestion(currentQuestion);
        }
    });

    // Prevent form submission if not all answered
    form.addEventListener('submit', function(e) {
        if (answeredQuestions.size !== questions.length) {
            e.preventDefault();
            alert("Please answer all questions before submitting the test.");
        }
    });

    // Initial setup
    submitBtn.disabled = true;  // 🚀 Force disabling Submit initially
    showQuestion(currentQuestion);
    updateProgressAndSubmit();
});
