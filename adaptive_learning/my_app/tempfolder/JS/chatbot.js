function toggleChatbot() {
    const popup = document.getElementById('chatbot-popup');
    popup.style.display = popup.style.display === 'flex' ? 'none' : 'flex';
    if (popup.style.display === 'flex') {
        populateVideoDropdown();
        // Reset selected video title display and input/button state
        document.getElementById('selected-video-title').textContent = '';
        document.getElementById('chat-input-box').disabled = true;
        document.getElementById('chat-send-btn').disabled = true;
    }
}

function populateVideoDropdown() {
    const select = document.getElementById('video-select');
    select.innerHTML = '<option value="">Select a video...</option>';
    document.querySelectorAll('.video-frame').forEach(frame => {
        const title = frame.getAttribute('data-video-title');
        if (title) {
            const option = document.createElement('option');
            option.value = title;
            option.textContent = title;
            select.appendChild(option);
        }
    });
}

document.getElementById('video-select').addEventListener('change', function() {
    window.selectedVideoTitle = this.value;
    const titleSpan = document.getElementById('selected-video-title');
    const chatBox = document.getElementById('chat-messages');
    if (this.value) {
        titleSpan.textContent = `Selected: ${this.value}`;
        document.getElementById('chat-input-box').disabled = false;
        document.getElementById('chat-send-btn').disabled = false;
        // Reset chat when video changes
        chatBox.innerHTML = '<div class="bot-message">You are now chatting about: <b>' + this.value + '</b></div>';
    } else {
        titleSpan.textContent = '';
        document.getElementById('chat-input-box').disabled = true;
        document.getElementById('chat-send-btn').disabled = true;
        chatBox.innerHTML = '';
    }
});

function sendMessage() {
    const inputBox = document.getElementById("chat-input-box");
    const message = inputBox.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat-messages");
    chatBox.innerHTML += `<div class="user-message">${message}</div>`;
    inputBox.value = "";

    const selectedVideoTitle = window.selectedVideoTitle;
    if (!selectedVideoTitle) {
        chatBox.innerHTML += `<div class="bot-message">Please select a video first.</div>`;
        return;
    }

    fetch(phi3ChatURL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('[name=csrf-token]').content
        },
        body: JSON.stringify({ message: message, video_title: selectedVideoTitle })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot-message">${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        chatBox.innerHTML += `<div><strong>Error:</strong> Something went wrong</div>`;
    });
}

document.getElementById("chat-input-box").addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !this.disabled) {
        event.preventDefault();
        sendMessage();
    }
});
