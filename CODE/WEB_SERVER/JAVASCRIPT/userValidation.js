function SignUp() {
    let userID = document.getElementById("i-new-username").value; // Get UserID from Field on Sign Up Page
    let password1 = document.getElementById("i-new-password").value; // Get's User's Init Password 
    let password2 = document.getElementById("i-password-confirm").value; // Gets User's Password Confirm
    // let model = document.getElementById("car-model").value; // Gets User's Car Deatails (Subject to change based on how data is stored)


    console.log(userID);
    // Check if UserID is taken...
    // >> User ID Check

    // Check if Init && Confirm Passwords Match
    if (password1 != password2) {
        DisplayError("Passwords Do Not Match!");
        return;
    }

    // >> STORE DATA

    return;
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