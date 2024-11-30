let button = document.getElementById("fullscreen-button");
// if (body.requestFullScreen) body.requestFullScreen();

button.addEventListener("click", function (e) {
  if (document.fullscreenElement) {
    fullscreenElement.exitFullscreen();
    button.innerText = "Enter Fullscreen";
  } else {
    fullscreenElement.requestFullscreen();
    button.innerText = "Exit Fullscreen";
  }
});

var text = document.getElementById("text");
text.innerHTML = "";

document.addEventListener("visibilitychange", () => {
  //   text.innerHTML = "";
  if (document.hidden) {
    // tab changed
    text.innerHTML += "Active";
  } else {
    // tab is active
    text.innerHTML += "Tab Changed";
  }
});
