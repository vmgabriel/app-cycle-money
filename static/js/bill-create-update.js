// Develop: vmgabriel

// Get Data
const getData = (data) => document.getElementById(data);

const switchClassName =
      (className) =>
      (element) =>
      (element.classList.contains(className))
      ? element.classList.remove(className)
      : element.classList.add(className);


function changeIsRepeter() {
    const data = getData('repeter-selector');
    switchClassName('hide')(data);
}
