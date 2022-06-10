function SignUpClicK(form) {
  SignUp(form);
  return false;
}

async function SignUp(form) {
  let userID = form.userID.value;
  let password1 = form.password1.value;
  let password2 = form.password2.value;

  FetchUserExists(userID).then((userExists) => {
    if (userExists) {
      DisplayError("Username Already In Use!");
      return false;
    } else if (CheckPassword(password1, password2)) {
      PostNewUser(userID, password1).then((id) => LoginUser(userID));
    }
  });
}
function CheckPassword(password1, password2) {
  if (password1 != password2) {
    DisplayError("Passwords Do Not Match!");
    return false;
  } else return true;
}
function SignInClicK(form) {
  console.log("already");
  SignIn(form);
  return false;
}

function SignIn(form) {
  let userID = form.userID.value;
  let password = form.password.value;

  FetchValidSignIn(userID, password).then((isValid) => {
    if (!isValid) {
      DisplayError("UserID and/or Password is Inccorect! here");
      return false;
    }
    console.log("valid");
    // Login User
    LoginUser(userID);
  });
}

function DisplayError(err) {
  try {
    ShowError(err);
  } catch {
    console.error(err);
    console.warn("Error container is not defined");
  }
  return;
}

// check fo an existing cookie
function CheckLogin() {
  let id = GetId();
  if (id != null) {
    /*FetchUserExists(id).then((existis) => {
      if (existis) {
        LoginUser(id);
      } else {
        // cookie is bad and should be deleted
        ClearUserCookie();
      }
    });*/
   // clear all cookies for now
  }
  ClearUserCookie();
}
