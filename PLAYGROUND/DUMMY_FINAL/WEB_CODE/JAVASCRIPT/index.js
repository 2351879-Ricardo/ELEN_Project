// This script is specifically condered with performing tasks in index.html when new useres arive at the site

const navPanel = document.getElementById("nav-panel");
const signUp = document.getElementById("sign-up-panel");
const signIn = document.getElementById("sign-in-panel");

const errorContainer = document.getElementById("error-display");

const hiddenClass = "no-display"; // CSS class given to object which must be hidden
let currentPanel = navPanel;

SetMainPanel(navPanel);

function SetMainPanel(panelId) {
  switch (panelId) {
    case navPanel.id:
      SetCurrentPanel(navPanel);
      ClearError();
      break;
    case signUp.id:
      SetCurrentPanel(signUp);
      ClearError();

      break;
    case signIn.id:
      SetCurrentPanel(signIn);
      ClearError();
      break;
  }
}

function SetCurrentPanel(panel) {
  if (panel != currentPanel) {
    HidePanel(currentPanel);
    ShowPanel(panel);
    currentPanel = panel;
  }
}

// panel is a css element
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

function ShowError(err) {
  errorContainer.innerHTML = err;
}

function ClearError(err) {
  errorContainer.innerHTML = "";
}
