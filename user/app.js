const express = require('express');
const mongoose = require('mongoose');
const user = require('./router/user.router');
const product = require('./router/product.router');

const app = express();
app.use(express.json());
app.use(express.urlencoded({extended:true}));

const mongoURL = process.env.MONGODBURL||'mongodb://localhost:27017/project';
mongoose.connect(mongoURL,{
    usenewUrlParser:true,
    useunifiedTOPOLOGY:true,
})
.then(()=>console.log('database connected successfully'))
.catch((err)=>console.log(err.message));

app.get('/',async(req,res)=>{
    res.send({message:"database is working"});
});

app.use('/',user);
app.use('/',product);

const PORT = process.env.PORT || 8000;
app.listen(PORT,()=>console.log(`http://localhost:${PORT}`));
