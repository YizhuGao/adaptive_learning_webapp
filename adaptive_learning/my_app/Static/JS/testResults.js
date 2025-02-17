document.addEventListener("DOMContentLoaded", function() {
    const scoreElement = document.querySelector(".score");
    const score = parseFloat(scoreElement.textContent);
    const feedbackContainer = document.getElementById("feedback-message");

    let message = "";
    let messageClass = "";

    if (score >= 80) {
        message = "🌟 Fantastic! You're a physics wizard! 🚀";
        messageClass = "success";
    } else if (score >= 50) {
        message = "✨ Good job! Keep pushing forward! 💪";
        messageClass = "warning";
    } else {
        message = "😓 Keep trying! Watch the videos and retake the test! 📚";
        messageClass = "error";
    }

    // Display the message
    feedbackContainer.textContent = message;
    feedbackContainer.classList.add("feedback-message", messageClass);

    // Fade out after a few seconds
    setTimeout(() => {
        feedbackContainer.style.opacity = "0";
    }, 5000);
});
