// This script checker weather or not the user is loged in on the frontend

// Login validation

function Test() {
  let t = document.getElementById("log-link");
  t.innerHTML = "good";
}

function onSignIn(googleUser) {
  alert("User signed in");
  let;
}

function getIdToken(googleUser) {
  return googleUser.getAuthResponse().id_token;
}

// returns current user data or null if user is not logged in
function GetUserData(){
  
}
