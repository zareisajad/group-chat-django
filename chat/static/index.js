// Automatically set the focus to the room name input
document.querySelector('#room-name-input').focus();
// If you hit "enter" on the keyboard, trigger the click method
document.querySelector('#room-name-input').onkeyup = (e) => {
    if (e.keyCode === 13) {
        document.querySelector('#room-name-submit').click();
    }
};
// When you submit the form, redirect the user to the room page
document.querySelector('#room-name-submit').onclick = (e) => {
    var roomName = document.querySelector('#room-name-input').value;
    var userName = document.querySelector('#username-input').value;
    window.location.replace(roomName + '/?username=' + userName);
};