/**
 * Hello world
 */

let http = require("http");
let server;

server = http.createServer((request, response) => {
    response.writeHead(200, {
        "Content-Type": "application/json"
    });
    response.end("Hello!", "utf-8");
    console.log(`url = ${request.url}`);
}).listen(4401);

console.log("Server started at `localhost:4401`, and will close in 60s...");

setTimeout(() => {
    console.log("Server shutdown");
    server.close();
}, 60000);

// ========================================
let ConfigUtils = require("./ConfigUtils");
let util = require("util");

console.log(`emailServer = ${ConfigUtils.EMAIL_SERVER()}`);
console.log(`remoteServer = ${ConfigUtils.REMOTE_URL()}`);
console.log(__dirname);
console.log(util.inspect(ConfigUtils.EMAIL_SERVER()));

// ==================================
let UrlUtils = require("./UrlUtils");
let url = "92304803?985=90458&3948=2937&jkdf=39&080";

console.log(`urlMap = ${JSON.stringify(UrlUtils.getUrlMap(url))}`);
