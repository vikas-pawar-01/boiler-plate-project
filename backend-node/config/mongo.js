const mongoose = require("mongoose");

const connectMongo = async () => {
  try {
    await mongoose.connect("mongodb://mongo:27017/app");
    console.log("MongoDB connected 🚀");
  } catch (err) {
    console.error(err);
  }
};

module.exports = connectMongo;
