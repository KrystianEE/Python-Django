var boxes = document.querySelectorAll("td")

function changem(){
  if (this.textContent == "") {
    this.textContent = "X";
  }
  else if (this.textContent == "X") {
    this.textContent = "O";
  }
  else {
    this.textContent = "";
  }
}


var restart=document.querySelector("#m")


console.log(restart)


function clearBoard(){
  for (var i = 0; i < boxes.length; i++) {
    boxes[i].textContent=""
  }
}



for (var i = 0; i < boxes.length; i++) {
  boxes[i].addEventListener("click", changem)
}

restart.addEventListener("click", clearBoard)
