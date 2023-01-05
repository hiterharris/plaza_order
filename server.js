const express = require("express");
const helmet = require("helmet");
const cors = require("cors");
const bodyParser = require("body-parser");

const OrderRouter = require("./router.js");

const server = express();

server.use(helmet());
server.use(express.json());
server.use(cors());
server.use(bodyParser.json());

server.get("/", (req, res) => {
  res.send("Plaza Order Online");
});

server.use("/order", OrderRouter);

module.exports = server;