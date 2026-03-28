const { Pool } = require("pg");

const pool = new Pool({
  host: "postgres",
  user: "dev",
  password: "dev",
  database: "app_db",
});

const mongoose = require("mongoose");

mongoose.connect("mongodb://mongo:27017/app");

