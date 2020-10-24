const express = require("express");
var https = require("follow-redirects").https;

const app = express();
app.use(function (req, res, next) {
  res.header(
    "Access-Control-Allow-Origin",
    "*"
  ); // update to match the domain you will make the request from
  res.header("Access-Control-Allow-Headers", "*");
  next();
});
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use("/d", (req, res) => {
    const { domain, path, cookie } = req.body;
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
  console.log(req.get("User-Agent"))
  let options = {
    method: "GET",
    hostname: "tika.egybest.com",
    path: url,
    headers: {
      "User-Agent":
          req.get("User-Agent"),
      Cookie: cookie,
    },
    maxRedirects: 20,
  };
  let req_1 = https.request(options, function (req_res) {
    let chunks = [];

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

  req_1.end();
});



app.all("*", (req, res) => {
  res.status(404).send({
    status: "Failed",
    err: "Unhandled Route. Error 404",
  });
  // res.send()
});

module.exports = app;
