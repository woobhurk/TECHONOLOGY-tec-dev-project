const { app, BrowserWindow } = require("electron");

app.whenReady().then(createWindow);

function createWindow() {
    // Create the browser window.
    let win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    // and load the index.html of the app.
    win.loadFile("index.html");
    console.log("Windows created.");
}
