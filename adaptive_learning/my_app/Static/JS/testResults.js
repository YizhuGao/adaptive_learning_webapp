// testResults.js

console.log("testResults.js is loading!");

document.addEventListener("DOMContentLoaded", function() {
    const scoreElement = document.querySelector(".score");
    const score = parseFloat(scoreElement.textContent);
    const feedbackContainer = document.getElementById("feedback-message");

    let message = "";
    let messageClass = "";

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

    // Display the message
    feedbackContainer.textContent = message;
    feedbackContainer.classList.add("feedback-message", messageClass);

    // Fade out after a few seconds
    setTimeout(() => {
        feedbackContainer.style.opacity = "0";
    }, 5000);

    // Ensure video watch flag is updated after video ends
    var player;  // Declare globally
var subtopicId = null; // Declare globally to be assigned later

document.addEventListener("DOMContentLoaded", function() {
    subtopicId = document.getElementById("learning-video").dataset.subtopicId; // Get from data attribute
    console.log("Subtopic ID:", subtopicId);

    // Ensure YouTube API script is loaded
    if (typeof YT === "undefined" || !YT.Player) {
        console.log("YouTube API script not found, adding it.");
        var script = document.createElement("script");
        script.src = "https://www.youtube.com/iframe_api";
        document.body.appendChild(script);
    } else {
        console.log("YouTube API already loaded.");
        onYouTubeIframeAPIReady(); // Manually call if already available
    }
});

// Move function OUTSIDE to make it globally available
function onYouTubeIframeAPIReady() {
    console.log("YouTube API ready, initializing player.");
    player = new YT.Player('learning-video', {
        events: {
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerStateChange(event) {
    if (event.data === YT.PlayerState.ENDED) {
        console.log("Video ended! Updating watch flag for subtopic:", subtopicId);
        updateWatchVideoFlag(subtopicId);
    }
}

function updateWatchVideoFlag(subtopicId) {
    console.log("Sending POST request to update-watch-video/" + subtopicId);

    fetch(`/update-watch-video/${subtopicId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "subtopic_id": subtopicId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Watch status updated successfully!");
        } else if (data.error) {
            alert("Error: " + data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while updating the flag.");
    });
}