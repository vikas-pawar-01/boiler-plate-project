const { Pool } = require("pg");

const pool = new Pool({
  host: "postgres",
  user: "dev",
  password: "dev",
  database: "app_db",
});

// 👇 ADD THIS
pool
  .connect()
  .then(() => console.log("Postgres connected 🚀"))
  .catch((err) => console.error("Postgres connection error ❌", err));

module.exports = pool;
