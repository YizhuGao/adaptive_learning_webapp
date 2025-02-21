document.addEventListener("DOMContentLoaded", function() {
    const watchButtons = document.querySelectorAll(".watch-btn");

    watchButtons.forEach(button => {
        button.addEventListener("mouseover", () => {
            button.style.transform = "scale(1.1)";
        });

        button.addEventListener("mouseout", () => {
            button.style.transform = "scale(1)";
        });
    });
});
