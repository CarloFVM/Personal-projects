var fname= prompt("Please let us know your first name: ");
var lname= prompt("Please let us know your last name: ");
var age= prompt("Please let us know your age: ");
var height=prompt("Please let us know your height: ");
var petname=prompt("Please let us know your pets name: ");
alert("Thank you so much for the information.")

var spyname=null;
var spyage=null;
var spyheight=null;
var spypet

if (fname[0]===lname[0]) {
  spyname=true

}else {
  spyname=false
}

if (age>=20 && age<=30) {
  spyage=true
}else {
  spyage=false
}

if (height>=170) {
  spyheight=true
}else {
  spyheight=false
}
if (petname[petname.length-1]==="y") {
  spypet=true
}else {
  spypet=false
}
if (spyname && spyage && spyheight && spypet) {
  console.log("Welcome Comrade! You've passed the Spy Test");
}else {
  console.log("nel");
}
