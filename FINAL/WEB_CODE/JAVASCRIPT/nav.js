const loginLandingPath = "./log.html";
const hiddenClass = "no-display"; // CSS class given to object which must be hidden

function LoginUser(userId) {
  SetUserCookie(userId);
  window.location = loginLandingPath;
}
function Logout() {
  ClearUserCookie();
  window.location = "./index.html";
}

// hide and show panels
function ShowPanel(panel) {
  if (panel.classList.contains(hiddenClass)) {
    panel.classList.remove(hiddenClass);
  }
}
function HidePanel(panel) {
  if (!panel.classList.contains(hiddenClass)) {
    panel.classList.add(hiddenClass);
  }
}

// populate dropdown bars
function AddOptions(selectElem, optionList) {
  optionList.forEach((element) => {
    let option = document.createElement("option");
    // remove spsaces to simply saving ect later on
    option.value = element;
    option.innerHTML = element;
    selectElem.appendChild(option);
  });
}
