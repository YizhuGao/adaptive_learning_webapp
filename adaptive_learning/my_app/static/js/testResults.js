console.log("testResults.js is loading!");

document.addEventListener("DOMContentLoaded", function () {
    const scoreElement = document.querySelector(".score");
    const score = parseFloat(scoreElement.textContent);
    const feedbackContainer = document.getElementById("feedback-message");

    let message = "";
    let messageClass = "";

    // Set feedback based on score
    if (score >= 80) {
        message = "Fantastic! You're a physics wizard!";
        messageClass = "success";
    } else if (score >= 50) {
        message = "Good job! Keep pushing forward!";
        messageClass = "warning";
    } else {
        message = "Keep trying! Watch the videos and retake the test!";
        messageClass = "error";
    }

    // Display feedback message
    feedbackContainer.textContent = message;
    feedbackContainer.classList.add("feedback-message", messageClass);

    // Fade out feedback after 5 seconds
    setTimeout(() => {
        feedbackContainer.style.opacity = "0";
    }, 5000);

    // Highlight correct and incorrect answers + update status
    const answerRows = document.querySelectorAll('.results-table tbody tr');
    answerRows.forEach(row => {
        const answerCell = row.querySelector('td:nth-child(2)'); // Second cell = selected answer
        const statusCell = row.querySelector('.status'); // Third cell = status
        
        if (statusCell.classList.contains('correct')) {
            answerCell.classList.add('correct-answer');
            statusCell.innerHTML = '✔️ Correct';
            statusCell.classList.add('correct');
        } else if (statusCell.classList.contains('incorrect')) {
            answerCell.classList.add('incorrect-answer');
            statusCell.innerHTML = '❌ Incorrect';
            statusCell.classList.add('incorrect');
        }
    });

    // Ensure navbar remains fixed and resizes correctly
    window.addEventListener('resize', () => {
        const navbar = document.querySelector('.navbar');
        if (window.innerWidth <= 768) {
            navbar.style.padding = '12px 20px';
        } else {
            navbar.style.padding = '15px 30px';
        }
    });

    // Scroll to top on page load
    window.scrollTo(0, 0);
});