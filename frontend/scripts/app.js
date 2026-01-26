const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatOutput = document.getElementById('chat-output');

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const userMessage = chatInput.value;
    appendMessage('user-message', userMessage);
    chatInput.value = '';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        appendMessage('bot-message', data.response);
    } catch (error) {
        console.error('Error:', error);
        appendMessage('bot-message', 'Sorry, there was an error processing your request.');
    }
});

function appendMessage(className, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', className);
    messageElement.innerHTML = message;
    chatOutput.appendChild(messageElement);
    chatOutput.scrollTop = chatOutput.scrollHeight; // Scroll to the bottom
}