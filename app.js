const { app, BrowserWindow, ipcMain, Menu } = require('electron');
const { exec } = require('child_process');
const path = require('path');
const preloadDirName = path.join(__dirname, '/components/preload/preload.js');

// create a new canvas window
function createWindow() {
    const win = new BrowserWindow({
        width: 600,
        height: 800,
        resizable: false,
        webPreferences: {
            preload: preloadDirName,
            nodeIntegration: true,
            contextIsolation: false,
        },
    });
    win.loadFile('./views/index.html');
    Menu.setApplicationMenu(null);
}

//configure default events
app.whenReady().then(() => {
    createWindow();
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

//drop window event
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

//execute script python
ipcMain.on('run-python', (event, args) => {
    console.log(args);
    exec(`python3 ./scripts/main.py ${args}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Erro: ${error.message}`);
            event.reply('python-result', `Erro: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            event.reply('python-result', `stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        event.reply('python-result', `Resultado: ${stdout}`);
    });
});
