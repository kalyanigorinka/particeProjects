const router = require('express').Router();
const mongoose = require('mongoose');
const product = require('../model/product.model');
const User = require('../model/user.model');


router.post('/addproduct',async(req,res)=> {
    const createparams = {
        Name:req.body.Name,
        UserId:req.body.UserId,
    }
    const newproduct = await product.create(createparams);
    if(newproduct){
        res.send({message:"product created successfully",data:newproduct})
    }else{
        res.send({message:"product created failed"})
    }
});

router.get('/allproduct',async(req,res)=>{
    const newproduct = await product.find();
    if(newproduct){
        res.send({message:"product data fetched successfully",data:newproduct})
    }else{
        res.send({message:"data not found"})
    }

});

router.post('/singleproduct',async(req,res)=>{
    const newproduct = await product.findById({"_id":req.body.id});
    if(newproduct){
        res.send({message:"product fetched successfully",data:newproduct})
    }else{
        res.send({message:"product not found"})
    }
});

router.post('/getproduct',async(req,res)=>{
    const newproduct = await product.findOne({"Name":req.body.Name});
    if(newproduct){
        const user = await User.findById({"_id":newproduct.UserId})
        res.send({
            message:"product fetched successfully",
            data:{
                productName:newproduct.Name,
                userName:user.firstName
            }
        })
    }else{
        res.send({message:"product not found"})
    }
});


router.post('/updateproduct',async(req,res)=>{
    const newproduct = await product.findByIdAndUpdate({"_id":req.body.id},{"Name":req.body.Name},{new:true})
    if(newproduct){
        res.send({message:"product updated successfully",data:newproduct})
    }else{
        res.send({message:"product updated failed"})
    }
});

router.post('/deleteproduct',async(req,res)=>{
    const newproduct = await product.findByIdAndRemove({"_id":req.body.id})
    if(newproduct){
        res.send({message:"product deleted successfully"})
    }else{
        res.send({message:"product deleted failed"})
    }
});



module.exports = router;
