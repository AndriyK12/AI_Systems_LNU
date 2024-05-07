const dropdownBtn = document.getElementById('dropdown-btn');
const dropdownMenu = document.getElementById('dropdown-menu');

dropdownBtn.addEventListener('click', () => {
    dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
});

const chatBotButton = document.getElementById('chat-bot-button');
const chatWindow = document.getElementById('chat-window');
const chatMessages = document.getElementById('chat-messages');
const chatInputText = document.getElementById('chat-input-text');
const chatSendButton = document.getElementById('chat-send-button');
const chatCloseButton = document.getElementById('chat-close-button');

chatBotButton.addEventListener('click', function() {
    chatWindow.style.display = 'block';
});

chatSendButton.addEventListener('click', async () => {
    const message = chatInputText.value.trim();
    if (message !== '') {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = "You: " + message;
        chatMessages.appendChild(messageDiv);
        chatInputText.value = '';
    }
    
    if (message !== '') {
        const response = await fetch('http://localhost:5000/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        const botMessage = data.response;

        const messageDiv = document.createElement('div');
        messageDiv.textContent = "Bot: " + botMessage;
        messageDiv.className = 'bot-message';
        chatMessages.appendChild(messageDiv);

        chatInputText.value = '';
    }
});

chatCloseButton.addEventListener('click', function() {
    chatWindow.style.display = 'none';
});