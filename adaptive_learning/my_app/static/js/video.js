// Function to mark the video as watched
function markVideoAsWatched(videoId, subtopicId, button) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    console.log(`Sending request to mark video ${videoId} as watched for subtopic ${subtopicId}`);

    fetch('/complete-video/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            video_id: videoId,
            subtopic_id: subtopicId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log(`Successfully marked video ${videoId} as watched.`);
            // Add the watched class to trigger the animation
            button.classList.add('watched');
            // Update button content
            button.querySelector('.button-content').innerHTML = `
                <i class="fas fa-check"></i>
                <span class="button-text">Watched</span>
            `;
            button.style.backgroundColor = '#4CAF50';
            
            // Find and update the corresponding button in the modal if it exists
            const modalButton = document.getElementById('modalMarkWatchedBtn');
            if (modalButton && modalButton.getAttribute('data-video-id') === videoId) {
                modalButton.classList.add('watched');
                modalButton.querySelector('.button-content').innerHTML = `
                    <i class="fas fa-check"></i>
                    <span class="button-text">Watched</span>
                `;
                modalButton.style.backgroundColor = '#4CAF50';
            }
        } else {
            console.error('Error marking video as watched:', data.message);
        }
    })
    .catch(error => {
        console.error('Error making request:', error);
    });
}

// Event listener for each "Mark as Watched" button
document.querySelectorAll('.mark-watched-btn').forEach(button => {
    button.addEventListener('click', function() {
        if (!this.classList.contains('watched')) {
            const videoId = this.getAttribute('data-video-id');
            const subtopicId = this.getAttribute('data-subtopic-id');

            console.log(`Button clicked for video ID: ${videoId}, subtopic ID: ${subtopicId}`);

            // Call the function to mark the video as watched
            markVideoAsWatched(videoId, subtopicId, this);
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const nav = document.querySelector('nav');
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Mobile menu toggle
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const mobileMenu = document.querySelector('.mobile-menu');

if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', function() {
        this.classList.toggle('active');
        mobileMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!mobileMenuBtn.contains(event.target) && !mobileMenu.contains(event.target)) {
            mobileMenuBtn.classList.remove('active');
            mobileMenu.classList.remove('active');
        }
    });
}
