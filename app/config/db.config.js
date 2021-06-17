module.exports = {
  HOST: "ivry.us.to",
  USER: "root",
  PASSWORD: "123",
  DB: "ivry",
  dialect: "mysql",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
};
