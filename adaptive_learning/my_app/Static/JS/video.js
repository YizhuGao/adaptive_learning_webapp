// Function to mark the video as watched
function markVideoAsWatched(videoId, subtopicId) {
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
    button.addEventListener('click', function () {
        const videoId = this.getAttribute('data-video-id');
        const subtopicId = this.getAttribute('data-subtopic-id');

        console.log(`Button clicked for video ID: ${videoId}, subtopic ID: ${subtopicId}`);

        // Call the function to mark the video as watched
        markVideoAsWatched(videoId, subtopicId);
    });
});
