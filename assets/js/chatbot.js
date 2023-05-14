// Chatbot
const form = document.getElementById('chatbot-form');
const input = document.getElementById('chatbot-input');
const container = document.querySelector('.chat-box-body');
const closeButton = document.getElementById('chatbot-close');
const chatButton = document.getElementById('chatButton');
const chatWindow = document.getElementById('chatWindow');
let savedMessages = [];

// Load saved messages from local storage
if (localStorage.getItem('chatbot-messages')) {
  savedMessages = JSON.parse(localStorage.getItem('chatbot-messages'));
  savedMessages.forEach(message => {
    const { sender, text } = message;
    const messageClass = sender === 'user' ? 'user-message' : 'chatbot-message';
    container.innerHTML += `<div class="${messageClass}">${text}</div>`;
  });
}

// Function to scroll to the bottom of the chat window
const scrollToBottom = () => {
  container.scrollTop = container.scrollHeight;
};

// Function to send a message to the chatbot
const sendMessage = message => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `/get_response/?message=${message}`);
  xhr.onload = () => {
    if (xhr.status === 200) {
      const response = xhr.responseText;
      container.innerHTML += `<div class="chatbot-message">${response}</div>`;
      // Save message to local storage
      savedMessages.push({ sender: 'chatbot', text: response });
      localStorage.setItem('chatbot-messages', JSON.stringify(savedMessages));
      // Scroll to bottom of chat window
      scrollToBottom();
    }
  };
  xhr.send();
};

// Event listener for form submission
form.addEventListener('submit', e => {
  e.preventDefault();
  const message = input.value.trim();
  if (message) {
    container.innerHTML += `<div class="user-message">${message}</div>`;
    // Save message to local storage
    savedMessages.push({ sender: 'user', text: message });
    localStorage.setItem('chatbot-messages', JSON.stringify(savedMessages));
    // Send message to chatbot and scroll to bottom of chat window
    sendMessage(message);
    scrollToBottom();
    input.value = '';
  }
});

// Event listener for close button
closeButton.addEventListener('click', () => {
  // Store chat history in local storage and clear messages
  localStorage.setItem('chatbot-messages', JSON.stringify(savedMessages));
  savedMessages = [];
  // Clear chat window
  container.innerHTML = '';
  chatWindow.classList.add('d-none');
});

// Event listener for chat button
chatButton.addEventListener('click', () => {
  chatWindow.classList.remove('d-none');
  scrollToBottom();
});
