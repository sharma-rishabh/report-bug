const main = () => {
  button = document.querySelector("#report-button");
  button.onclick = () => alert("reported");
};

window.onload = main;
