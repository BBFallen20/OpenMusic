let play = function () {
    let x = document.getElementById("track-med");
    x.play();
    setTimeout(() => { x.pause(); }, 15000);
}