// This sicript is BAD.
// It must be fixed to access the data base

const userId = "jeff";

// Vehcile class
class Vehicle {
  constructor(name, fuel, type, uservehicle = false) {
    this.name = name;
    this.fuel = fuel;
    this.type = type;
    this.userVehicle = uservehicle;
  }

  get displayName() {
    let prefix = "average ";
    if (this.userVehicle) {
      prefix = "your ";
    }
    return prefix + this.name;
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
    return this.type;
  }
}

function GetUserVehicles() {
  let vCount = 1;
  vCount = parseInt(vCount);
  let userVehicles = [];
  for (let i = 0; i < vCount; i++) {
    // userVehicles.push(GetVehicle(true));
    userVehicles.push(new Vehicle("User car " + i, "petrol", "hatchback"));
  }
  return userVehicles;
}

function GetUserTravelData(userVehicle, dateFrom, dateTo) {
  let userData = new TravelData(
    userVehicle,
    Math.random() * 1000,
    Math.random() * 100
  );
  return userData;
}
function GetGeneralTravelData(vehicle) {
  return new TravelData(vehicle, Math.random() * 1000, Math.random() * 100);
}

function GetVehicle(forUser) {
  alert("would fecth vechile... for user: " + forUser);
  let name = prompt("what is it's name");
  let fuel = prompt(
    "what type of fuel does it use: petrol, diesel, or electric"
  );
  let energy = prompt("How much energy did it use?");
  energy = parseFloat(energy);
  let distance = prompt("how far dd the vehicle travle");
  distance = parseFloat(distance);
  return new Vehicle(name, fuel, energy, distance, forUser);
}

// Get fuels types (Mock DB)
function GetFuelTypes() {
  return ["petrol", "diesel", "electric"];
}

function GetCarTypes(fuelType) {
  switch (fuelType) {
    case "petrol":
      return [
        "SUV",
        "hatchback",
        "crossover",
        "convertable",
        "sedan",
        "sports car",
        "coupe",
        "minivan",
        "4x4",
        "motorbike",
      ];
    case "diesel":
      return [
        "SUV",
        "hatchback",
        "crossover",
        "minivan",
        "4x4",
        "pickup truck",
        "truck",
        "tank",
      ];
    case "electric":
      return ["SUV", "sedan", "sports car", "4x4", "pickup truck"];
    default:
      throw "unknown type " + fuelType;
  }
}

function GetModels(fuel, type) {
  return [
    fuel + " " + " " + type + " boi",
    fuel + " " + " " + type + " bar",
    fuel + " " + " " + type + " foo",
  ];
}

//  date collection
function GetFirstUserEntry() {
  return "2021-12-29";
}
function GetToday() {
  let today = new Date();
  let day = ("0" + today.getDate()).slice(-2);
  let month = ("0" + (today.getMonth() + 1)).slice(-2);
  let year = today.getFullYear();
  return year + "-" + month + "-" + day;
}

// Login data validation
