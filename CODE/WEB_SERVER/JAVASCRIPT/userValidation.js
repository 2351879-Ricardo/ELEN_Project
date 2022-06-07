function SignUp() {
    let userID = document.getElementById("i-new-username").value; // Get UserID from Field on Sign Up Page
    let password1 = document.getElementById("i-new-password").value; // Get's User's Init Password 
    let password2 = document.getElementById("i-password-confirm").value; // Gets User's Password Confirm

    // userExists = (PYTHON >> UserExists(userID) >> returns true or false)
    if (userExists) {
        DisplayError("Username Already In Use!");
        return;
    }

    // Check if Init && Confirm Passwords Match
    if (password1 != password2) {
        DisplayError("Passwords Do Not Match!");
        return;
    }

    // Login User
    LoginUser(userID);
}

function SignIn() {
    let userID = document.getElementById("i-username").value; // Get UserID 
    let password = document.getElementById("i-password").value; // Gets User's Entered Password

    // isValid = (PYTHON >> IsValidSignIn(userID, password) >> returns true or false)

    if (!isValid) {
        DisplayError("UserID and/or Password is Inccorect!");
        return;
    }

    // Login User
    LoginUser(userID);
}

function callbackFunc(response) {
    console.log(response);
    return;
}

function DisplayError(err) {
    console.log(err); // Current Test Code For Debug
    // >> DISPLAY ERROR TO FRONT-END
    return;
}