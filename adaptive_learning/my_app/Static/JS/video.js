//console.log("video.js is loading!");
//
//document.addEventListener("DOMContentLoaded", function () {
//    console.log("Learning video page loaded.");
//
//    // Get the video URL and IDs from the data attributes
//    const playerContainer = document.getElementById("player");
//    const subtopicId = playerContainer.getAttribute("data-subtopic-id");
//    const studentId = playerContainer.getAttribute("data-student-id");
//    const videoUrl = playerContainer.getAttribute("data-video-url");
//
//    console.log("Video URL:", videoUrl);
//    console.log("Subtopic ID:", subtopicId);
//    console.log("Student ID:", studentId);
//
//    // Ensure the video URL is available
//    if (!videoUrl) {
//        console.error("No video URL found.");
//        return;
//    }
//
//    // If URL is valid, initialize the YouTube player with the URL directly
//    if (videoUrl.includes("youtube.com") || videoUrl.includes("youtu.be")) {
//        console.log("Found YouTube URL, initializing player...");
//        initYouTubePlayer(videoUrl, subtopicId, studentId);
//    } else {
//        console.error("The video URL is not a valid YouTube URL.");
//    }
//});
//
//// Function to initialize the YouTube player
//function initYouTubePlayer(videoUrl, subtopicId, studentId) {
//    console.log("Initializing YouTube player with URL:", videoUrl);
//
//    // Create a div to hold the YouTube player
//    const playerDiv = document.createElement("div");
//    playerDiv.id = "youtube-player";
//    document.getElementById("player").appendChild(playerDiv);
//
//    // Initialize the YouTube player using the embed URL directly
//    new YT.Player(playerDiv, {
//        height: '450',
//        width: '800',
//        videoId: videoUrl.split("/").pop(), // Using the last part of the URL for embedding
//        playerVars: {
//            autoplay: 1,
//            mute: 1,
//            controls: 1,
//            rel: 0,
//            showinfo: 0,
//        },
//        events: {
//            'onReady': function(event) {
//                console.log("YouTube player is ready!");
//                event.target.playVideo(); // Start the video
//            },
//            'onStateChange': function(event) {
//                console.log("Player state changed:", event.data);
//                switch (event.data) {
//                    case YT.PlayerState.ENDED:
//                        console.log("Video has ended.");
//                        markVideoAsWatched(subtopicId, studentId);
//                        break;
//                    case YT.PlayerState.PLAYING:
//                        console.log("Video is playing.");
//                        break;
//                    case YT.PlayerState.PAUSED:
//                        console.log("Video is paused.");
//                        break;
//                    default:
//                        console.log("Unknown player state:", event.data);
//                }
//            }
//        }
//    });
//}
//
//// Function to mark the video as watched and notify the server
//function markVideoAsWatched(subtopicId, studentId) {
//    console.log("Sending request to update progress...");
//
//    fetch("/update-progress/", {
//        method: 'POST',
//        headers: {
//            'Content-Type': 'application/json',
//            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').content
//        },
//        body: JSON.stringify({
//            'subtopic_id': subtopicId,
//            'student_id': studentId
//        })
//    })
//    .then(response => response.json())
//    .then(data => {
//        console.log("Progress updated successfully:", data);
//    })
//    .catch(error => {
//        console.error("Error updating progress:", error);
//    });
//}


console.log("video.js is loading!");

// Wait for the page to fully load
window.onload = function() {
    console.log("Learning video page loaded.");

    // Get the video URL and IDs from the data attributes
    const playerContainer = document.getElementById("player");

    if (!playerContainer) {
        console.error("Player container not found!");
        return;
    }

    const subtopicId = playerContainer.getAttribute("data-subtopic-id");
    const studentId = playerContainer.getAttribute("data-student-id");
    const videoUrl = playerContainer.getAttribute("data-video-url");

    console.log("Video URL:", videoUrl);
    console.log("Subtopic ID:", subtopicId);
    console.log("Student ID:", studentId);

    // Ensure the video URL is available
    if (!videoUrl) {
        console.error("No video URL found.");
        return;
    }

    // If URL is valid, initialize the YouTube player with the URL directly
    if (videoUrl.includes("youtube.com") || videoUrl.includes("youtu.be")) {
        console.log("Found YouTube URL, initializing player...");
        initYouTubePlayer(videoUrl, subtopicId, studentId);
    } else {
        console.error("The video URL is not a valid YouTube URL.");
    }
};

// Function to initialize the YouTube player
function initYouTubePlayer(videoUrl, subtopicId, studentId) {
    console.log("Initializing YouTube player with URL:", videoUrl);

    // Create a div to hold the YouTube player
    const playerDiv = document.createElement("div");
    playerDiv.id = "youtube-player";
    document.getElementById("player").appendChild(playerDiv);

    // Initialize the YouTube player using the embed URL directly
    new YT.Player(playerDiv, {
        height: '450',
        width: '800',
        videoId: videoUrl.split("/").pop(), // Using the last part of the URL for embedding
        playerVars: {
            autoplay: 1,
            mute: 1,
            controls: 1,
            rel: 0,
            showinfo: 0,
        },
        events: {
            'onReady': function(event) {
                console.log("YouTube player is ready!");
                event.target.playVideo(); // Start the video
            },
            'onStateChange': function(event) {
                console.log("Player state changed:", event.data);
                switch (event.data) {
                    case YT.PlayerState.ENDED:
                        console.log("Video has ended.");
                        markVideoAsWatched(subtopicId, studentId);
                        break;
                    case YT.PlayerState.PLAYING:
                        console.log("Video is playing.");
                        break;
                    case YT.PlayerState.PAUSED:
                        console.log("Video is paused.");
                        break;
                    default:
                        console.log("Unknown player state:", event.data);
                }
            }
        }
    });
}

// Function to mark the video as watched and notify the server
function markVideoAsWatched(subtopicId, studentId) {
    console.log("Sending request to update progress...");

    // Check that studentId is a valid number
    if (!studentId || isNaN(studentId)) {
        console.error("Invalid student ID:", studentId);
        return; // Don't proceed if the student ID is invalid
    }

    fetch("/update-progress/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').content
        },
        body: JSON.stringify({
            'subtopic_id': subtopicId,
            'student_id': studentId
        })
    })
    .then(response => response.json())  // Expecting a JSON response from the server
    .then(data => {
        if (data.status === 'success') {
            console.log("Progress updated successfully:", data);

            // After updating, redirect the user to the test page for the current topic and subtopic
            setTimeout(function() {
                // Redirect to the test page after 1 minute
                window.location.href = "/test/" + data.topic_name + "/" + data.subtopic_name + "/";
            }, 60000);
        } else {
            console.error("Error:", data.message);  // Log any error message from the server
        }
    })
    .catch(error => {
        console.error("Error updating progress:", error);
    });
}
