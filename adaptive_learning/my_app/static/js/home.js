document.addEventListener("DOMContentLoaded", () => {
    const welcomeText = document.querySelector(".welcome-text");

    function updateGreeting() {
        const hour = new Date().getHours();
        let greeting = "Hello";
        if (hour < 12) greeting = "Good Morning";
        else if (hour < 18) greeting = "Good Afternoon";
        else greeting = "Good Evening";

        const name = welcomeText.textContent.split(",")[1]?.trim() || "";
        welcomeText.textContent = `${greeting}, ${name}`;
    }

    updateGreeting();
    setInterval(updateGreeting, 60000); // Update every minute
});
