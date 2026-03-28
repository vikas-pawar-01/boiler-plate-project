const redis = require("redis");

const client = redis.createClient({
  url: "redis://redis:6379",
});

client.on("connect", () => {
  console.log("Redis connected 🚀");
});

module.exports = client;
