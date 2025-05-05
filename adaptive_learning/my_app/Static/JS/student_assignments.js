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

document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('scoreChart').getContext('2d');

    const scoreChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartLabels,
            datasets: [
                {
                    label: 'Score Before',
                    data: chartScoreBefore,
                    borderColor: 'blue',
                    backgroundColor: 'rgba(0, 0, 255, 0.1)',
                    fill: false,
                    tension: 0.2,
                    spanGaps: true
                },
                {
                    label: 'Score After',
                    data: chartScoreAfter,
                    borderColor: 'red',
                    backgroundColor: 'rgba(255, 0, 0, 0.1)',
                    fill: false,
                    tension: 0.2,
                    spanGaps: true
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top'
                },
                title: {
                    display: true,
                    text: 'Progress by Subtopic'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 120
                }
            }
        }
    });
});
