const http = require("http");

// Import configs
const pool = require("./config/db");
const connectMongo = require("./config/mongo");
const redisClient = require("./config/redis");

// Connect Mongo
connectMongo();

// Connect Redis
redisClient.connect();

const server = http.createServer(async (req, res) => {
  if (req.url === "/api/test") {
    // Test Postgres
    const result = await pool.query("SELECT NOW()");

    // Test Redis
    await redisClient.set("test", "Hello Redis");

    res.end(
      JSON.stringify({
        postgres: result.rows[0],
        redis: "OK",
      })
    );
  } else {
    res.end("Node API running 🚀");
  }
});

server.listen(5001, () => {
  console.log("Server running on port 5001");
});
