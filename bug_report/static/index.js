const API = {
  postBugReport: (reqDetails) => fetch("/api/report-bug", reqDetails),
};

const takeScreentshot = () =>
  html2canvas(document.body).then((canvas) => {
    return canvas.toDataURL();
  });
const sendBugReport = async () => {
  const headers = { "Content-Type": "application/json" };
  const screentshot = await takeScreentshot();
  const dom = document.head.outerHTML + document.body.outerHTML;
  const body = JSON.stringify({
    message: "there is a bug",
    screentshot,
    dom,
  });
  return API.postBugReport({ method: "POST", headers, body })
    .then((res) => res.json())
    .then((data) => console.log(data));
};

const main = () => {
  button = document.querySelector("#report-button");
  button.onclick = () => sendBugReport();
};

window.onload = main;
