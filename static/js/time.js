const socket = io(); // Establish websocket connection

socket.on('connect', () => {
    console.log("time connected");
})

socket.on('disconnect', () => {
    console.log("time disconnected");
})

socket.on('time_update', function(data) {
    console.log(data.time);
    document.getElementById('time').innerHTML = data.time;
})