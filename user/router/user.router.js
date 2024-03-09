const router = require('express').Router();
const mongoose = require('mongoose');
const User = require('../model/user.model');
const Product = require('../model/product.model');



router.post('/addUser',async(req,res)=> {
    const createparams = {
        firstName:req.body.firstName,
        email:req.body.email,
    }
    const newUser = await User.create(createparams);
    if(newUser){
        res.send({message:"User created successfully",data:newUser})
    }else{
        res.send({message:"User created failed"})
    }
});

router.get('/allUser',async(req,res)=>{
    const newUser = await User.find();
    if(newUser){
        res.send({message:"Users data fetched successfully",data:newUser})
    }else{
        res.send({message:"data not found"})
    }

});

router.post('/singleUser',async(req,res)=>{
    const newUser = await User.findById({"_id":req.body.id});
    if(newUser){
        res.send({message:"User fetched successfully",data:newUser})
    }else{
        res.send({message:"User not found"})
    }
});

router.post('/userProducts',async(req,res)=>{
    const newUser = await User.findOne({"firstName":req.body.firstName});
    if(newUser){
        const products = await Product.find({UserId:newUser._id})
        res.send({
            message:"User fetched successfully",
            data:newUser,
            products:products
        })
    }else{
        res.send({message:"User not found"})
    }
});

router.post('/updateUser',async(req,res)=>{
    const newUser = await User.findByIdAndUpdate({"_id":req.body.id},{"firstName":req.body.firstName},{new:true})
    if(newUser){
        res.send({message:"User updated successfully",data:newUser})
    }else{
        res.send({message:"user updated failed"})
    }
});

router.post('/deleteUser',async(req,res)=>{
    const newUser = await User.findByIdAndRemove({"_id":req.body.id})
    if(newUser){
        res.send({message:"User deleted successfully"})
    }else{
        res.send({message:"user deleted failed"})
    }
});

module.exports = router;