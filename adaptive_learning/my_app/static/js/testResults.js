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

    // Get the score and feedback message elements
    const scoreValue = parseInt(document.querySelector('.score').textContent);
    const feedbackMessage = document.getElementById('feedback-message');

    // Animate score counting up
    const animateValue = (start, end, duration) => {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const currentValue = Math.floor(progress * (end - start) + start);
            scoreElement.textContent = `${currentValue}%`;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    };

    // Start score animation
    animateValue(0, score, 1500);

    // Function to set feedback message based on score
    function setFeedbackMessage(scoreValue) {
        let message = '';
        let icon = '';
        let className = '';
        let emoji = '';

        if (scoreValue >= 90) {
            message = 'Outstanding! You have mastered this topic!';
            icon = 'trophy';
            className = 'success';
            emoji = '🎉';
        } else if (scoreValue >= 75) {
            message = 'Great job! Keep up the good work!';
            icon = 'star';
            className = 'success';
            emoji = '👏';
        } else if (scoreValue >= 60) {
            message = 'Good effort! Review the material to improve further.';
            icon = 'book';
            className = 'warning';
            emoji = '📚';
        } else {
            message = 'Keep practicing! Watch the video lesson to strengthen your understanding.';
            icon = 'video';
            className = 'error';
            emoji = '💪';
        }

        feedbackMessage.innerHTML = `
            <div class="feedback-box ${className}">
                <i class="fas fa-${icon}"></i>
                ${message} ${emoji}
            </div>
        `;

        // Add animation class after a small delay
        setTimeout(() => {
            feedbackMessage.querySelector('.feedback-box').classList.add('show');
        }, 100);
    }

    // Set initial feedback message
    setTimeout(() => {
        setFeedbackMessage(scoreValue);
    }, 1000);

    // Add hover effect to table rows with smooth animation
    const tableRows = document.querySelectorAll('.results-table tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', () => {
            row.style.transform = 'translateX(10px)';
            row.style.transition = 'all 0.3s ease';
            row.style.backgroundColor = 'rgba(158, 27, 50, 0.02)';
        });
        row.addEventListener('mouseleave', () => {
            row.style.transform = 'translateX(0)';
            row.style.backgroundColor = 'transparent';
        });
    });

    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.watch-video-button, .start-btn, .nav-link');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            this.appendChild(ripple);

            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Add smooth scroll behavior for navigation links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add intersection observer for fade-in animations
    const observerOptions = {
        root: null,
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements for fade-in
    const elements = document.querySelectorAll('.results-container > *, .learning-section');
    elements.forEach(el => {
        el.classList.add('fade-in-hidden');
        observer.observe(el);
    });

    // Add parallax effect to background
    document.addEventListener('mousemove', (e) => {
        const moveX = (e.clientX - window.innerWidth / 2) * 0.01;
        const moveY = (e.clientY - window.innerHeight / 2) * 0.01;
        document.body.style.backgroundPosition = `calc(50% + ${moveX}px) calc(50% + ${moveY}px)`;
    });

    // Initialize circular progress
    const circle = document.querySelector('.progress-ring__circle-fg');
    if (circle) {
        const radius = circle.r.baseVal.value;
        const circumference = 2 * Math.PI * radius;
        const score = parseInt(circle.dataset.score);

        // Set the initial state
        circle.style.strokeDasharray = `${circumference} ${circumference}`;
        circle.style.strokeDashoffset = circumference;

        // Animate the progress
        setTimeout(() => {
            const offset = circumference - (score / 100) * circumference;
            circle.style.strokeDashoffset = offset;
        }, 100);
    }

    // Add fade-in animation to elements
    const fadeElements = document.querySelectorAll('.results-container > *');
    fadeElements.forEach((element, index) => {
        element.classList.add('fade-in-hidden');
        setTimeout(() => {
            element.classList.add('fade-in');
        }, index * 100);
    });

    // Generate feedback message based on score
    const scoreElement = document.querySelector('.score');
    if (scoreElement) {
        const scoreValue = parseInt(scoreElement.textContent);
        const feedbackMessage = document.getElementById('feedback-message');
        
        let feedbackContent = '';
        let feedbackClass = '';
        
        if (scoreValue >= 90) {
            feedbackContent = '<i class="fas fa-trophy"></i> Outstanding! You\'ve mastered this topic!';
            feedbackClass = 'success';
        } else if (scoreValue >= 75) {
            feedbackContent = '<i class="fas fa-star"></i> Great work! Keep up the good effort!';
            feedbackClass = 'success';
        } else if (scoreValue >= 60) {
            feedbackContent = '<i class="fas fa-arrow-up"></i> You\'re making progress! A bit more practice will help.';
            feedbackClass = 'warning';
        } else {
            feedbackContent = '<i class="fas fa-book"></i> Keep learning! Review the material and try again.';
            feedbackClass = 'error';
        }

        if (feedbackMessage) {
            const messageBox = document.createElement('div');
            messageBox.className = `feedback-box ${feedbackClass}`;
            messageBox.innerHTML = feedbackContent;
            feedbackMessage.appendChild(messageBox);

            setTimeout(() => {
                messageBox.classList.add('show');
            }, 300);
        }
    }
});