const loginLandingPath = "./log.html";

// A lightwiht fron end validation and naviagtion system
// = Requires cookie moster for funtionality
function CheckLogin() {
  let id = GetId();
  if (id != null) {
    console.log(id);
    // CHeck to see if id is valid
    // Cannot use becuase server is broken
    /*FetchUserExists(id).then((existis) => {
      if (existis) {
        LoginUser(id);
      } else {
        // cookie is bad and should be deleted
        ClearUserCookie();
      }
    });*/
    ClearUserCookie(); // clear all cookies for now
  }
}
function LoginUser(userId) {
  SetUserCookie(userId);
  window.location = loginLandingPath;
}
function Logout() {
  ClearUserCookie();
}
