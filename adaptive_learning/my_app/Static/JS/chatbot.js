function toggleChatbot() {
    const popup = document.getElementById('chatbot-popup');
    popup.style.display = popup.style.display === 'flex' ? 'none' : 'flex';
}

function sendMessage() {
    const inputBox = document.getElementById("chat-input-box");
    const message = inputBox.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat-messages");
    // chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    chatBox.innerHTML += `<div class="user-message">${message}</div>`;
    inputBox.value = "";

    // fetch("/phi3_chat/", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //         "X-CSRFToken": document.querySelector('[name=csrf-token]').content
    //     },
    //     body: JSON.stringify({ message: message })
    // })
    fetch(phi3ChatURL, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector('[name=csrf-token]').content
    },
    body: JSON.stringify({ message: message })
})
    .then(response => response.json())
    .then(data => {
        // chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
        chatBox.innerHTML += `<div class="bot-message">${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        chatBox.innerHTML += `<div><strong>Error:</strong> Something went wrong</div>`;
    });
}

document.getElementById("chat-input-box").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
