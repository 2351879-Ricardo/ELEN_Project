// Requires fetch.js and cookieMonster
const logPanel = document.getElementById("log-panel");
const newLogPanel = document.getElementById("new-log-panel");
CheckLog();

//Check to see if the user has a log already
function CheckLog() {
  id = GetId();
  FetchServer(id, "/log/exists").then((exists) => {
    if (!exists) {
      HidePanel(logPanel);
      ShowPanel(newLogPanel);
      SetNewLog();
    }
  });
}

// setup new log panel
function SetNewLog() {
  GetServer("/database/types").then((response) => {
    fuelTypes = response[0]["fuel"];
    vehicelTypes = response[0]["vehicle"];

    let fuelSelect = document.getElementById("fuel-select");
    let vehicleSelect = document.getElementById("vehicle-select");
    AddOptions(fuelSelect, fuelTypes);
    AddOptions(vehicleSelect, vehicelTypes);
  });
}

// Creteast a new log for the user
function MakeLog(form) {
  console.log(",make");
  OnMakeLog(form);
  return false;
}

function OnMakeLog(form) {
  logData = {
    userID: GetId(),
    fuel: form.fuel,
    vehicle: form.vehicle,
  };

  console.log(logData);

  FetchServer(logData, "/log/create").then((response) => {
    console.log("log made" + response);
    HidePanel(newLogPanel);
    ShowPanel(logPanel);
  });
}

// Data collection
function SumbitLogPost(form) {
  OnSubmitLogPost(form);
  return false;
}

function OnSubmitLogPost(form) {
  id = GetId();

  logData = {
    userID: GetId(),
    logDate: form.logDate,
    odometer: form.odometer,
    aveFuel: form.aveFuel,
  };

  FetchServer(logDate, "/log/post").then("log posted");
}
