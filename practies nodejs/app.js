const express = require("express");
const mongoose =require("mongoose");

const app=express();
app.use(express((urlencoded),{extends:true}))
app.use(express.json());

const mongoURL = process.env.MONGODBURL ||'mongodb://localhost:27017/test';
mongoose.connect(mongoURL,{
    usenewurlparser:true,
    useunfieldtopology:true
})

.then(()=>console.log("database connected sucsessfully"))
.catch((err)=>console.log(err.message));

app.get('/',async(req,res)=>{
    res.send({message:"ok api is working"})
})

const PORT = process.env.PORT||3000;
app.listen(PORT,()=>console.log(`http://localhost:${PORT}`))


// const { urlencoded } = require("express");
// const express = require("express");
// const mongoose =require("mongoose");

// const app = express();
// app.use(express((urlencoded),{extends:true}))
// app.use(express.json());

// const mongoURL=process.env.MONGODBURL||'mongodb://localhost:27017/test';
// mongoose.connect(mongoURL,{
//    UseNewURLParser:true,
//    useunifiedTOPOLOGY:true 
// })



// .then(()=>console.log("database connected sucsessfully"))
// .catch((err)=>console.log(err.message));

// app.get('/',async(req,res)=>{
//     res.send ({message:"ok api is working"})
// })


// const PORT =process.env.PORT||4000;
// app.listen(PORT,()=>console.log(`http://localhost:${PORT}`))





