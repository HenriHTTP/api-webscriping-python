// renderer.js
const { ipcRenderer } = require('electron');

//excute python script on click event
document.getElementById('run-python-btn').addEventListener('click', () => {
  const amount = document.getElementById('amount').value;
  const selectedFields = Array.from(
    document.querySelectorAll('input[type="checkbox"]:checked'),
  ).map((checkbox) => checkbox.value);
  const file_name = document.getElementById('name-csv').value;
  const args = `"${selectedFields.join(',')}" ${amount} ${file_name}`;
  document.getElementById('output').innerHTML =
    '<img src="./public/img/loading.gif" alt="Loading..." style="width: 50px; height: 50px; margin:auto;">';
  console.log(args);
  ipcRenderer.send('run-python', args);
});

// recive python executation
ipcRenderer.on('python-result', (event, result) => {
  document.getElementById('output').innerText = result;
});
