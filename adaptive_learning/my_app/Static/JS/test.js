document.addEventListener("DOMContentLoaded", () => {
    const questions = document.querySelectorAll(".question-card");
    const progressBar = document.getElementById("progress");
    const nextBtn = document.getElementById("next-btn");
    const prevBtn = document.getElementById("prev-btn");

    let currentQuestion = 0;
    const totalQuestions = questions.length;
    let answeredQuestions = new Set();

    // Show first question
    questions[currentQuestion].classList.add("active");

    // Handle next button
    nextBtn.addEventListener("click", () => {
        if (currentQuestion < totalQuestions - 1) {
            questions[currentQuestion].classList.remove("active");
            currentQuestion++;
            questions[currentQuestion].classList.add("active");
            updateButtons();
        }
    });

    // Handle previous button
    prevBtn.addEventListener("click", () => {
        if (currentQuestion > 0) {
            questions[currentQuestion].classList.remove("active");
            currentQuestion--;
            questions[currentQuestion].classList.add("active");
            updateButtons();
        }
    });

    // Handle answer selection
    questions.forEach((question, index) => {
        question.querySelectorAll("input[type='radio']").forEach(radio => {
            radio.addEventListener("change", () => {
                answeredQuestions.add(index);
                updateProgressBar();
            });
        });
    });

    // Update buttons state
    function updateButtons() {
        prevBtn.disabled = currentQuestion === 0;
        nextBtn.disabled = currentQuestion === totalQuestions - 1;
    }

    // Update progress bar
    function updateProgressBar() {
        const progress = (answeredQuestions.size / totalQuestions) * 100;
        progressBar.style.width = `${progress}%`;
    }

    updateButtons();
});
