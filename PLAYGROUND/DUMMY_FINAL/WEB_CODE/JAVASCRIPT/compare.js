// Spesifally made for the compare page

const vehicleTemplate = document.getElementById("vehicle");
const dateFromInput = document.getElementById("date-start");
const dateToInput = document.getElementById("date-end");
const submitButton = document.getElementById("b-sumbit-compare");

const vehicleList = document.getElementById("vehicle-list");
const addVehiclePanel = document.getElementById("add-vehicle");
const addvehicleButton = document.getElementById("b-add-vehicle");
const fuelSelect = document.getElementById("fuel-select");
const typeSelect = document.getElementById("vehicle-select");

const userVehicles = [];
const comparedVehicles = [];
const compLimit = 5;

OnDocLoad();

class Vehicle {
  constructor(name, fuel, type, uservehicle = false) {
    this.name = name;
    this.fuel = fuel;
    this.type = type;
    this.userVehicle = uservehicle;
  }

  get displayName() {
    let display = this.name;
    if (this.fuel != "all") {
      display += " " + this.fuel;
    }
    if (this.type != "all") {
      display += " " + this.type;
    }
    return display;
  }
}
class TravelData {
  constructor(vehicle, energyUsed, distance) {
    this.vehicle = vehicle;
    this.energyUsed = energyUsed;
    this.distance = distance;
  }
  get AverageConsumption() {
    return this.energyUsed / this.distance;
  }

  get energyUse() {
    return this.energyUsed;
  }

  get distanceTravelled() {
    return this.distance;
  }

  get type() {
    return this.vehicle;
  }
}
// called when from is submitted
function GetTravelData(form) {
  RequestData(form);
  return false;
}
function RequestData(form) {
  let userRequest = {
    userID: GetId(),
    dateStart: form.dateStart.value,
    dateEnd: form.dateEnd.value,
  };
  let otherRequest = [];
  comparedVehicles.forEach((v) => {
    otherRequest.push({
      fuel: v.fuel,
      vehicle: v.type,
      dateStart: form.dateStart.value,
      dateEnd: form.dateEnd.value,
    });
  });
  let travelReports = [];
  FetchServer(userRequest, "/database/userlog")
    .then((userData) => {
      let userReport = new TravelData(
        userVehicles[0],
        userData[0]["energy"],
        userData[0]["distance"]
      );
      travelReports.push(userReport);
    })
    .then(
      FetchServer(otherRequest, "/database/average").then((response) => {
        for (let i = 0; i < comparedVehicles.length; i++) {
          travelReports.push(
            new TravelData(
              comparedVehicles[i],
              response[i]["energy"],
              response[i]["distance"]
            )
          );
        }
        DrawEnergyChart(travelReports);
      })
    );
}

function OnDocLoad() {
  FetchServer(GetId(), "/log/vehicle").then((vehicleData) => {
    let vehicle = new Vehicle(
      "your",

      vehicleData[0]["fuel"],
      vehicleData[0]["vehicle"]
    );
    let elem = MakeVehicelElem(vehicle, true);
    userVehicles.push(vehicle); // support for the possiblity of multiple user vihicles in future
    SetFormDefaults();
  });

  GetServer("/database/types").then((types) => {
    let fuelTypes = types[0]["fuel"];
    AddOptions(fuelSelect, fuelTypes);
  });
}

// adding vehilces to a list

function MakeVehicelElem(vehcile, isUserVehicle = false) {
  let newClone = vehicleTemplate.content.firstElementChild.cloneNode(true);
  vehicleList.insertBefore(newClone, addVehiclePanel);
  let cloneName = newClone.getElementsByClassName("p-name")[0];
  let cloneFuel = newClone.getElementsByClassName("p-fuel")[0];
  let cloneType = newClone.getElementsByClassName("p-type")[0];
  cloneName.innerHTML = vehcile.name;
  cloneFuel.innerHTML = vehcile.fuel;
  cloneType.innerHTML = vehcile.type;
  newClone.listVehicle = vehcile;
  SetRemoveButton(newClone, isUserVehicle);

  return newClone;
}

function RemoveVehicleElem(elem) {
  for (let i = 0; i < comparedVehicles.length; i++) {
    if (comparedVehicles[i] == elem.listVehicle) {
      comparedVehicles.splice(i, 1);
      break;
    }
  }
  elem.parentNode.removeChild(elem);
  submitButton.disabled = comparedVehicles.length == 0;
  addvehicleButton.disabled = comparedVehicles.length >= compLimit;
  return false;
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

function OnFuelChange(fuel) {
  RemoveOptions(typeSelect);
  typeSelect.disabled = true;
  if (fuel == "all") {
    typeSelect.disabled = true;
  } else {
    FetchServer(fuel, "/database/offueltype").then((typeList) => {
      AddOptions(typeSelect, typeList);
      typeSelect.disabled = false;
    });
  }
}
function AddInputVehicle() {
  let inputVehicle = GetInputVehicle();
  MakeVehicelElem(inputVehicle);
  comparedVehicles.push(inputVehicle);
  addvehicleButton.disabled = comparedVehicles.length >= compLimit;
  submitButton.disabled = comparedVehicles.length == 0;
  fuelSelect.value = "all";
  typeSelect.value = "all";
  return false;
}
function GetInputVehicle() {
  let fuel = fuelSelect.value;
  let type = typeSelect.value;
  return new Vehicle("Average", fuel, type);
}

function RemoveOptions(selector) {
  let option = selector.lastElementChild;
  while (option && option.value != "all") {
    selector.removeChild(option);
    option = selector.lastElementChild;
  }
}
