function OnSignUpClicK() {
  console.log("testsst");
  SignUp();
  return false;
}

async function SignUp() {
  let userID = document.getElementById("i-new-username").value; // Get UserID from Field on Sign Up Page
  let password1 = document.getElementById("i-new-password").value; // Get's User's Init Password
  let password2 = document.getElementById("i-password-confirm").value; // Gets User's Password Confirm

  FetchUserExists(userID).then((userExists) => {
    console.log(userExists);
    if (userExists) {
      DisplayError("Username Already In Use!");
      return false;
    } else if (CheckPassword(password1, password2)) {
      PostNewUser(userID, password1).then(/*LoginUser(userID);*/);
    }
  });
}
function CheckPassword(password1, password2) {
  if (password1 != password2) {
    DisplayError("Passwords Do Not Match!");
    return;
  }
}

function SignIn() {
  let userID = document.getElementById("i-username").value; // Get UserID
  let password = document.getElementById("i-password").value; // Gets User's Entered Password

  // isValid = (PYTHON >> IsValidSignIn(userID, password) >> returns true or false)
  FetchValidSignIn(userID, password).then((isValid) => {
    if (!isValid) {
      DisplayError("UserID and/or Password is Inccorect!");
      return false;
    }

    // Login User
    LoginUser(userID);
  });
}

function DisplayError(err) {
  console.log(err); // Current Test Code For Debug
  // >> DISPLAY ERROR TO FRONT-END
  return;
}
