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
    // Update the greeting every minute
    setInterval(updateTime, 60000);

    // Smooth scrolling for internal links (if you have anchors)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href")).scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        });
    });

    // Add subtle animation to the welcome text when it loads
    welcomeText.classList.add("fade-in");

    // CSS animation for fade-in effect (added dynamically)
    const style = document.createElement("style");
    style.innerHTML = `
        .fade-in {
            animation: fadeIn 2s ease-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);

    // For the Get Started button, let's add smooth behavior
    const getStartedButton = document.querySelector('.btn-cta');
    if (getStartedButton) {
        getStartedButton.addEventListener("click", function(e) {
            e.preventDefault();
            document.querySelector("#modules").scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        });
    }
});
