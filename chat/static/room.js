document.querySelector('#chat-message-input').onkeyup = (e) => {
  if (e.keyCode === 13) {
      document.querySelector('#chat-message-submit').click();
  }
};

function scrollToBottom() {
  let objDiv = document.getElementById("chat-messages");
  objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();

const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);

const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/'
  + roomName
  + '/'
);

chatSocket.onmessage = (e) => {
  const data = JSON.parse(e.data);
  if(data.message) {
    document.querySelector('#chat-messages').innerHTML += ('<b>' + data.username + '</b>: ' + data.message + '<br>');
  };
  scrollToBottom();
}

chatSocket.onclose = (e) => {
  console.error('The socket closed!!!');
}

document.querySelector('#chat-message-submit').onclick = (e) => {
  const messageInput = document.querySelector('#chat-message-input');
  const message = messageInput.value;
  chatSocket.send(JSON.stringify({
    'message': message,
    'username': userName,
    'room': roomName
  }));
  messageInput.value = '';
};