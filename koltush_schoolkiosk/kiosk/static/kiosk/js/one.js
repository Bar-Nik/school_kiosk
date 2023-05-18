let buttons = document.querySelectorAll(".block_2 .button_floor");
let blocks = document.querySelectorAll(".one");
let activeButtonIndex = null; // variable to track the active button
const resetButton = document.getElementById("resetButton");

buttons.forEach((btn, index) => {
  btn.addEventListener("click", function(e) {
    if (activeButtonIndex === index) {
      // turn off action
      activeButtonIndex = null;
      if (blocks[index]) {
        blocks[index].classList.remove("run");
      }
    } else {
      // turn on action
      if (activeButtonIndex !== null) {
        if (blocks[activeButtonIndex]) {
          blocks[activeButtonIndex].classList.remove("run");
        }
      }
      activeButtonIndex = index;
      if (blocks[index]) {
        blocks[index].classList.add("run");
      }
    }
  });
});

resetButton.addEventListener('click', function(e) {
  if (activeButtonIndex !== null) {
    if (blocks[activeButtonIndex]) {
      blocks[activeButtonIndex].classList.remove('run');
    }
    activeButtonIndex = null;
  }
});



