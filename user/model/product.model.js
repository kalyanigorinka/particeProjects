const mongoose = require('mongoose');

const product = new mongoose.Schema({
    Name:{
        type:String,
        required:true,
    },
    Model:{
        type:String,
        // required:true,
    },

    year:{
        type:String,
        // required:true,
    },
    UserId:{ 
        type: String,
        required:true,
    },
    Status:{
        type:String,
        // required:true,
    },
    createdAt:{
        type: Date,
        default: new Date(),
    },
    updatedAt:{
        type: Date,
        default: new Date(),
    },

});

module.exports = mongoose.model('product', product);

