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

chatBotButton.addEventListener('click', function () {
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
            body: JSON.stringify({message})
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

chatCloseButton.addEventListener('click', function () {
    chatWindow.style.display = 'none';
});

document.getElementById("likeButton").addEventListener("click", function () {
    var message = this.getAttribute("data-message"); // Отримуємо значення з атрибута data-message
    fetch('http://localhost:5000/addInterest', {
        method: 'POST',
        body: JSON.stringify({message: message}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Відповідь від сервера:', data);
            document.getElementById('statusMessage').innerText = `Запит на додавання інтересу "${data.message}" успішно оброблено.`;
        })
        .catch(error => {
            console.error('Помилка:', error);
            document.getElementById('statusMessage').innerText = 'Помилка при відправленні запиту.';
        });
});

document.getElementById("recommendationButton").addEventListener("click", function () {
    fetch('http://localhost:5000/generateRecommendation')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            console.log('Рекомендація:', data);
            document.getElementById('recommendationResult').innerText = data;
        })
        .catch(error => {
            console.error('Помилка:', error);
            document.getElementById('recommendationResult').innerText = 'Помилка при отриманні рекомендації.';
        });
});