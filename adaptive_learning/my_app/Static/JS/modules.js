document.addEventListener("DOMContentLoaded", function() {
    const welcomeText = document.querySelector(".welcome-text");

    // Function to update the greeting message based on the time of day
    function updateTime() {
        const now = new Date();
        const hours = now.getHours();
        const greeting = hours < 12 ? "Good Morning" : hours < 18 ? "Good Afternoon" : "Good Evening";

        // Update the greeting with the username
        welcomeText.textContent = `${greeting}, ${welcomeText.textContent.split(",")[1]}`;
    }

    // Initial call to update greeting message
    updateTime();
    setInterval(updateTime, 60000);
});
