const { app, BrowserWindow } = require("electron");

app.whenReady().then(createWindow);

function createWindow() {
    // Create the browser window.
    let window = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    // Load the index.html of the app.
    window.loadFile("index.html");
    console.log("Windows created.");
}
