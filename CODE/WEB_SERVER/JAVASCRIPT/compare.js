// Spesifally made for the compare page

const compareRequest = document.getElementById("comp-request");
compareRequest.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log("submit");
  FetchData("jeff");
});

function FetchData(type) {
  alert("Would fet from data but ill just ask you");
  prompt("Entery the energy used by " + type);
}
function FetchVehciles(fuel, type) {}

function OnDocLoad() {}

function LoadVehicles() {
  let userVehicle = FetchData("User vehcle");
  let otherVechicle = FetchData("Default compariason vehcile");
}
