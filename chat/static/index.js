// Automatically set the focus to the room name input
document.querySelector('#room-name-input').focus();

// When you submit the form, redirect the user to the room page
document.querySelector('#room-name-submit').onclick = (e) => {
    var roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = roomName;
};