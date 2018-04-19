alert("This is a totaly legit site, don't worry")

var answers = 0
//here i will log corect answers

var name = prompt("Please tell me your name")

var surname = prompt("Please tell me your last name")

if (name[0]==surname[0]){
  answers++;
}

prompt("Whats up?")
alert("thats nice")


var age = prompt("How old are you ?")

if (age >= 20 && age <= 30){
  answers++
}

var height = prompt("How high are you (not stoned)(in cm)?")

if (height>=170){
  answers++
}

var petname = prompt("Whats your pet's name?")

if (petname[petname.length - 1] == "y"){
  answers++
}


if (answers == 4){
  alert("Sup spy?")
}
