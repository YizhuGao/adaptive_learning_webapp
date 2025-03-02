console.log("video.js is loading!");

// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    console.log("Learning video page loaded.");

    // Fetch the video element
    var video = document.getElementById("learning-video");

    // Ensure the video element exists before attaching the event listener
    if (video) {
        console.log("Video element found!");

        // Listen for the 'play' event, which is fired when the video starts playing
        video.addEventListener("play", function () {
            console.log("Video started playing!");  // This should print when the video starts
            markVideoAsWatched();  // Update the progress flag immediately
        });

        // Listen for the 'canplay' event to ensure we get the correct video duration
        video.addEventListener("canplay", function () {
            console.log("Video Duration: " + video.duration);  // Logs the video duration
        });

        // Monitor video progress
        video.addEventListener("timeupdate", function () {
            var videoProgress = (video.currentTime / video.duration) * 100;
            console.log("Video progress: " + videoProgress.toFixed(2) + "%");

            // You can update the flag after the video reaches 75%, but for now, we do it at play
            if (videoProgress >= 75) {
                console.log("75% of the video watched");
                // markVideoAsWatched(); // Uncomment to also update progress at 75%
            }
        });
    } else {
        console.log("Video element not found!");
    }

    // Function to notify the server when the video starts playing
    function markVideoAsWatched() {
        const subtopicId = document.getElementById("learning-video").getAttribute("data-subtopic-id");
        const studentId = document.getElementById("learning-video").getAttribute("data-student-id");

        fetch("/update-progress/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value
            },
            body: JSON.stringify({
                'subtopic_id': subtopicId,
                'student_id': studentId
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Optional: to log the server response
        })
        .catch(error => {
            console.error("Error updating progress:", error);
        });
    }
});
