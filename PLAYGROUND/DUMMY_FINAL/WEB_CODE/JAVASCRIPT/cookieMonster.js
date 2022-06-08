// This script is resposible for cecking that a user is logged in and returning their

const idCookieName = "bsicuitBoi";
const lifeDays = 7;

// =========================================
// Genric cookie methods

// Return the value of a spcfic cookie
function GetCookie(cookieName) {
  let decodedCookie = decodeURIComponent(document.cookie);
  let cookieArray = decodedCookie.split(";");
  let nameExpression = cookieName + "=";
  let value = null;
  cookieArray.forEach((cookie) => {
    cookie = cookie.trim();
    if (cookie.indexOf(nameExpression) == 0) {
      value = cookie.substring(nameExpression.length, cookie.length);
    }
  });
  return value;
}

// Make a cookie with the given name and value
function SetCookie(name, value, days = lifeDays) {
  expires = GetExpiry(days);
  document.cookie = name + "=" + value + "; " + expires + "; path=/;";
}
// Delet a cookie with the given name
function DeleteCookie(name) {
  expires = GetExpiry(-100);
  document.cookie = name + "=; " + expires + "; path=/;";
}

function GetExpiry(days) {
  let date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  return (expires = "expires=" + date.toUTCString());
}

// =========================================
// Id cookie methods

function GetId() {
  let idCookie = GetCookie(idCookieName);
  return idCookie;
}
function SetUserCookie(userId) {
  SetCookie(idCookieName, userId);
}

function ClearUserCookie() {
  DeleteCookie(idCookieName);
}
