document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("table tr");

    rows.forEach((row) => {
        row.addEventListener("mouseenter", () => {
            row.style.backgroundColor = "#f0f0f0";
        });

        row.addEventListener("mouseleave", () => {
            row.style.backgroundColor = "";
        });
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
