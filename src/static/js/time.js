// const socket = io(); // Establish websocket connection

// socket.on('connect', () => {
//     console.log("time connected");
// })

// socket.on('disconnect', () => {
//     console.log("time disconnected");
// })

// socket.on('time_update', function(data) {
//     console.log(data.time);
//     document.getElementById('time').innerHTML = data.time;
// })

function currentTime() {
    var date = new Date();
    var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var months = ["January", "February", "Mars", "April", "May", "June", "July", "August", "September", "October", "November","December"];

    var hour = date.getHours();
    var min = date.getMinutes();

    hour = updateTime(hour);
    min = updateTime(min);

    var day = days[date.getDay()];
    var month = months[date.getMonth()];

    var time = hour + ":" + min;

    document.querySelector(".time").innerHTML = time;
    document.querySelector(".date").innerHTML = day + ", " + month + " " + date.getDate();
        var t = setTimeout(function(){ currentTime() }, 1000);
}

function updateTime(k) {
    if (k < 10) {
        return "0" + k;
    } else {
        return k;
    }
}

currentTime();