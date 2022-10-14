const API = {
  postBugReport: (reqDetails) => fetch("/api/report-bug", reqDetails),
};

// const getScreentshot = () =>
//   html2canvas(document).then((canvas) => {
//     canvas.toBlob((blob) => console.log(blob));
//   });

const sendBugReport = () => {
  const headers = { "Content-Type": "application/json" };
  // getScreentshot();
  const body = JSON.stringify({ message: "there is a bug" });
  return API.postBugReport({ method: "POST", headers, body });
};

const main = () => {
  button = document.querySelector("#report-button");
  button.onclick = sendBugReport;
};

window.onload = main;
