// This sicript is BAD. 
// It must be fixed to access the data base


// Vehcile class
class vehicle {
  constructor(name, fuel, type, averageEnergy, user = false) {
    this.name = name;
    this.fuel = fuel;
    this.type = type;
    this.averageEnergy = averageEnergy;
    this.user = user;
  }
}

function GetUserVehicles() {
  let vCount = prompt("How many vehcles does the user have?").parseInt();
  let userVehicles = [];
  for (let i = 0; i < vCount; i++) {
    userVehicles.push(GetVehicle(true));
  }
  return userVehicles;
}

function GetVehicle(forUser) {
  alert("would fecth vechile... for user: " + forUser);
  let name = prompt("what is it's name");
  let fuel = prompt(
    "what type of fuel does it use: petrol, diesel, or electric"
  );
  let energy = prompt("what us it's average energy consumption").parseFloat();
  return new vehicle(name, fuel, averageEnergy, forUser);
}
