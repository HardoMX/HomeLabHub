var modal = document.getElementById("modal");

var button = document.getElementById("modalButton");

var close = document.getElementById("close");


button.onclick = function() {
    modal.style.display = "block";
}

close.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function() {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
