const chatBox = document.getElementById('chatBox');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');

chatForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const msg = userInput.value;
    if (msg.trim() === '') return;
    appendMessage('user', msg);
    userInput.value = '';
    // Simulate AI response
    setTimeout(() => {
        appendMessage('ai', 'This is a sample AI response.');
    }, 700);
});

function appendMessage(sender, text) {
    const div = document.createElement('div');
    div.className = sender === 'user' ? 'user-msg mb-2' : 'ai-msg mb-2';
    div.innerHTML = `<span class="badge bg-${sender === 'user' ? 'primary' : 'success'}">${sender === 'user' ? 'You' : 'AI'}</span> <span>${text}</span>`;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}
