const mongoose = require('mongoose');
const users = new mongoose.Schema({
    firstName:{
        type: String,
        required: true,
    },
    lastName:{
        type: String,
        // required: true,
    },
    email:{
        type: String,
        required: true,
    },

    mobileNumber:{
        type: String,
        // required: true,
    },
    gender:{
        type: String,
        // required: true,
    },
    createdAt:{
        type: Date,
        default: new Date(),
    },updatedAt:{
        type: Date,
        default: new Date(),
    },
});

module.exports = mongoose.model('user',users);