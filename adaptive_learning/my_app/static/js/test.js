document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.question-card');
    const progressBar = document.querySelector('.progress');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const buttonContainer = document.querySelector('.button-container');
    
    let currentQuestionIndex = 0;
    const totalQuestions = questions.length;

    // Initialize progress and show first question immediately
    updateProgress();
    showQuestion(0);

    // Previous button click handler
    prevBtn.addEventListener('click', () => {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            showQuestion(currentQuestionIndex);
            updateProgress();
        }
    });

    // Next button click handler
    nextBtn.addEventListener('click', () => {
        if (currentQuestionIndex < totalQuestions - 1) {
            currentQuestionIndex++;
            showQuestion(currentQuestionIndex);
            updateProgress();
        }
    });

    // Add change event listeners to all radio inputs
    document.querySelectorAll('input[type="radio"]').forEach(radio => {
        radio.addEventListener('change', () => {
            updateProgress();
            checkAllQuestionsAnswered();
            
            // Auto-advance to next question after selection
            if (currentQuestionIndex < totalQuestions - 1) {
                setTimeout(() => {
                    currentQuestionIndex++;
                    showQuestion(currentQuestionIndex);
                    checkAllQuestionsAnswered(); // Check again after advancing
                }, 500); // Short delay before advancing
            } else {
                checkAllQuestionsAnswered(); // Check when on last question
            }
        });
    });

    function showQuestion(index) {
        // Hide all questions first
        questions.forEach(question => {
            question.style.display = 'none';
            question.classList.remove('active');
        });

        // Show the current question
        if (questions[index]) {
            questions[index].style.display = 'block';
            questions[index].classList.add('active');
            
            // Ensure the question is visible
            questions[index].scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }

        // Update current question index
        currentQuestionIndex = index;
    }

    function updateProgress() {
        const answeredQuestions = document.querySelectorAll('input[type="radio"]:checked').length;
        const progress = (answeredQuestions / totalQuestions) * 100;
        progressBar.style.width = `${progress}%`;
        
        // Update the questions answered counter
        document.getElementById('questions-answered').textContent = answeredQuestions;
    }

    function checkAllQuestionsAnswered() {
        const answeredQuestions = document.querySelectorAll('input[type="radio"]:checked').length;
        const submitContainer = document.querySelector('.submit-container');
        if (answeredQuestions === totalQuestions) {
            submitContainer.classList.add('show');
        } else {
            submitContainer.classList.remove('show');
        }
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft' && !prevBtn.disabled) {
            prevBtn.click();
        } else if (e.key === 'ArrowRight' && !nextBtn.disabled) {
            nextBtn.click();
        }
    });

    // Initial setup
    showQuestion(0); // Show first question immediately
    updateProgress(); // Initialize progress bar
    checkAllQuestionsAnswered(); // Check if any questions are already answered
});
