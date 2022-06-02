const chartCalls = "chart"; // all elements with this class will be made into charts
const chartTypleAttribute = "chart-type";
const dataTypeAtttribute = "id";

const chartOptions = {
  scales: {
    x: {
      beginAtZero: true,
      gridLines: {
        display: true,
        color: "rgb(78, 0, 73)",
        lineWidth: 3,
        zeroLineWidth: 3,
        zeroLineColor: "#2C292E",
      },
    },
  },
  indexAxis: "y",
  backgroundColor: [
    "rgb(78, 0, 73)",
    "rgba(255, 159, 64, 0.2)",
    "rgba(255, 205, 86, 0.2)",
    "rgba(75, 192, 192, 0.2)",
    "rgba(54, 162, 235, 0.2)",
    "rgba(153, 102, 255, 0.2)",
    "rgba(201, 203, 207, 0.2)",
  ],
  borderColor: [
    "rgb(163, 0, 153)",
    "rgb(255, 159, 64)",
    "rgb(255, 205, 86)",
    "rgb(75, 192, 192)",
    "rgb(54, 162, 235)",
    "rgb(153, 102, 255)",
    "rgb(201, 203, 207)",
  ],
  borderWidth: 1,
  borderRadius: 50,
  barPercentage: 0.5,
  categoryPercentage: 1.0,
  responsive: true,
  maintainAspectRatio: true,
};

// Called on doccument load
MakeCharts();

function MakeCharts() {
  console.log("hmm");
  let charts = document.getElementsByClassName("chart");
  Array.from(charts).forEach((chartElem) => {
    let data = GetChartData(chartElem);
    MakeChart(chartElem.id, chartElem.getAttribute(chartTypleAttribute), data);
  });
}

function MakeChart(id, type, data) {
  new Chart(id, {
    type: type,
    data,
    options: chartOptions,
  });
}

// Anamaytics fetching funtions
function GetChartData(chartElem) {
  let dataType = chartElem.getAttribute(dataTypeAtttribute);
  switch (dataType) {
    case "test":
      return [1, 2];
    case "energy":
      return GetEnergyData();

    default:
      break;
  }
}

function GetLables() {
  return ["you", "Other car"];
}
function GetEnergyData() {
  let data = {
    labels: GetLables(),
    datasets: [
      {
        label: "Total Energy used",
        data: GetEnergyValues(),
      },
    ],
  };
  return data;
}
function GetEnergyValues() {
  console.log("NB! Energy data system is tempory");
  return [Math.random() * 1000, Math.random() * 1000];
}
