const express = require("express");
var https = require("follow-redirects").https;

const app = express();
app.use(function (req, res, next) {
  res.header(
    "Access-Control-Allow-Origin",
    "chrome-extension://cfhbdgdkbcndjiikdmffkjanbgipjhfg"
  ); // update to match the domain you will make the request from
  res.header("Access-Control-Allow-Headers", "*");
  next();
});
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use("/d", (req, res) => {
    const { domain, path, cookie } = req.body;
    console.log(req.body);
    var options = {
      method: "GET",
      hostname: domain.replace("https://",""),
      path: path,
      headers: {
        Cookie: cookie,
      },
      maxRedirects: 20,
    };
  
    var req = https.request(options, function (req_res) {
      var chunks = [];
  
      req_res.on("data", function (chunk)  {
        chunks.push(chunk);
      }); 
  
      req_res.on("end", function (chunk) {
        var body = Buffer.concat(chunks);
        res.send(body.toString());
      });
  
      req_res.on("error", function (error) {
        console.error(error);
      });
    });
  
    req.end();
  });
app.use("/", (req, res) => {
  const { url, cookie } = req.body;
  var options = {
    method: "GET",
    hostname: "tika.egybest.com",
    path: url,
    headers: {
      "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
      Cookie: cookie,
    },
    maxRedirects: 20,
  };
  var req = https.request(options, function (req_res) {
    var chunks = [];

    req_res.on("data", function (chunk) {
      chunks.push(chunk);
    });

    req_res.on("end", function (chunk) {
      res.json({ url: req_res.responseUrl });
    });

    req_res.on("error", function (error) {
      console.error(error);
    });
  });

  req.end();
});



app.all("*", (req, res) => {
  res.status(404).send({
    status: "Failed",
    err: "Unhandled Route. Error 404",
  });
  // res.send()
});

module.exports = app;
