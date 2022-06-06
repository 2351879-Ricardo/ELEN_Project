// This script is resposible for cecking that a user is logged in and returning their

const idCookieName = "bsicuitBoi";

// Return the value of a spcfic cookie
function GetCookie(cookieName) {
  let decodedCookie = decodeURIComponent(document.cookie);
  console.log(decodedCookie);
}
function SetCookie(name, value) {
  document.cookie = name + "=" + value + ";path=/";
}

// Create a new cookie with the useres ID

// check to see if a user id cookie exists
function checkId() {
  let idCookie = GetCookie(idCookieName);
}
// Placholder
function MakeUserCookie(userId) {}
