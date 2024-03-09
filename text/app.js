const express = require('express');
const mongoose = require('mongoose');
const User = require('./user');
const Photo = require('./photo.js');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use('/', User);
app.use('/', Photo);


// const mongoURI=process.env.MONGODBURI || 'mongodb://localhost:27017/test';

mongoose.connect('mongodb+srv://deeperapp:deeperapp@cluster0.xypxa.mongodb.net/TEST?retryWrites=true&w=majority',{
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log("Database connected successfully"))
.catch((err) => console.log(err.message));

app.get("/", async (req, res) => {
  res.send({ message: "Ok api is working" });
});

const PORT = process.env.PORT || 8081;
app.listen(PORT, () => console.log(`http://localhost:${PORT}`));