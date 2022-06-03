// Spesifally made for the compare page

const vehicleTemplate = document.getElementById("vehicle");
const compareRequest = document.getElementById("comp-request");
const dateFromInput = document.getElementById("date-start");
const dateToInput = document.getElementById("date-end");

const vehicleList = document.getElementById("vehicle-list");
const addVehiclePanel = document.getElementById("add-vehicle");
const fuelSelect = document.getElementById("fuel-select");
const typeSelect = document.getElementById("type-select");
const modelSelect = document.getElementById("model-select");
const optionTemplate = document.getElementById("option-template");

const userVehicles = [];
const comparedVehicles = [];
compareRequest.addEventListener("submit", (e) => {
  e.preventDefault();
  RequestData();
});

OnDocLoad();

function RequestData() {
  AddInputVehicle();
  let travelReports = GetUserReports();
  travelReports.push(...GetGeneralReports());
  console.log(travelReports);
  DrawEnergyChart(travelReports);
}

function GetUserReports() {
  let reports = [];
  userVehicles.forEach((vehicle) => {
    reports.push(
      GetUserTravelData(vehicle, dateFromInput.value, dateToInput.value)
    );
  });
  return reports;
}

function GetGeneralReports() {
  let reports = [];
  comparedVehicles.forEach((vehicle) => {
    reports.push(GetGeneralTravelData(vehicle));
  });
  return reports;
}

function OnDocLoad() {
  let vehciles = GetUserVehicles();
  vehciles.forEach((vehicle) => {
    let elem = MakeVehicelElem(vehicle, true);
    userVehicles.push({ vehicle });
  });

  SetFormDefaults();
  SetAddVehicleUpdates();
}

// adding vehilces to a list

function MakeVehicelElem(vehcile, userVehcile) {
  let newClone = vehicleTemplate.content.firstElementChild.cloneNode(true);
  vehicleList.insertBefore(newClone, addVehiclePanel);
  let cloneName = newClone.getElementsByClassName("p-name")[0];
  let cloneFuel = newClone.getElementsByClassName("p-fuel")[0];
  let cloneType = newClone.getElementsByClassName("p-type")[0];
  cloneName.innerHTML = vehcile.name;
  cloneFuel.innerHTML = vehcile.fuel;
  cloneType.innerHTML = vehcile.type;
  //SetRemoveButton(newClone, userVehcile);

  return newClone;
}

function SetRemoveButton(newClone, userVehcile) {
  let removeButton = newClone.getElementsByClassName("b-action")[0];
  if (userVehcile) {
    removeButton.disabled = true;
    removeButton.innerHTML = "user vehicle";
  }
}

// Populate form with default values
function SetFormDefaults() {
  dateFromInput.defaultValue = GetFirstUserEntry();
  dateToInput.defaultValue = GetToday();
}

// Getting input form add-vehcile panel ===================================================
function SetAddVehicleUpdates() {
  fuelSelect.addEventListener("change", (e) => UpdateCarType(fuelSelect.value));
  typeSelect.addEventListener("change", (e) => UpdateModel(typeSelect.value));
}

function UpdateCarType(fuel) {
  RemoveOptions(typeSelect);
  RemoveOptions(modelSelect);
  modelSelect.disabled = true;
  if (fuel == "all") {
    typeSelect.disabled = true;
  } else {
    let vehicleTypes = GetCarTypes(fuel);
    AddOptions(typeSelect, vehicleTypes);
    typeSelect.disabled = false;
  }
}
function UpdateModel(type) {
  RemoveOptions(modelSelect);
  if (type == "all") {
    modelSelect.disabled = true;
  } else {
    let models = GetModels(fuelSelect.value, type);
    AddOptions(modelSelect, models);
    modelSelect.disabled = false;
  }
}
function AddInputVehicle() {
  comparedVehicles.push(GetInputVehicle());
}
function GetInputVehicle() {
  let fuel = fuelSelect.value;
  let type = typeSelect.value;
  let model = modelSelect.value;
  return new vehicle(model, fuel, type);
}

// option adding

function AddOptions(selector, values) {
  values.forEach((value) => {
    AddOption(selector, value);
  });
}
function AddOption(selector, optionValue) {
  clone = optionTemplate.content.firstElementChild.cloneNode(true);
  clone.innerHTML = optionValue;
  clone.value = optionValue;
  selector.append(clone);
}

function RemoveOptions(selector) {
  let option = selector.lastElementChild;
  while (option && option.value != "all") {
    selector.removeChild(option);
    option = selector.lastElementChild;
  }
}
