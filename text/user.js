const router = require("express").Router();
const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");
const User = require("./model");
const { isAuth } = require("./auth");

router.get("/", async (req, res) => {
  res.send({ message: "Ok api is working" });
});

router.post("/signup", async (req, res) => {
  try {
    const {fullName, email,password} = req.body;
    const UserExistHere = await User.findOne({ email });
    if (UserExistHere) {
      res.status(226).send({ msg: "User Already Registered here" });
    }
    const HashedPassword = bcrypt.hashSync(password,10)

    const createParams ={
      fullName: fullName,
      email: email,
      password: HashedPassword,
    };
    const NewUser = await User.create(createParams)
    if (NewUser) {
      const accessToken = jwt.sign(
        {
          _id: NewUser._id,
          fullName: NewUser.fullName,
          email: NewUser.email,
        },
        'screct',
        {
          expiresIn: '48h',
        })
      if (accessToken) {
        res.status(201).send({ msg: "User registration success",token: accessToken, Response: NewUser });
      }
    }else{
      res.status(500).send({ msg: "user registration failed" });
    }
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

router.post("/signin", async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email && !password) {
      res.status(404).send("please enter all feild");
    }
    const validUser =await User.findOne({email});
    if (!validUser) {
      res.status(404).send({ msg: "User Not Found" });
    }else{
      const isMatch = bcrypt.compareSync(password, validUser.password)
      if (validUser && isMatch) {
        const accessToken = jwt.sign(
          {
            _id: validUser._id,
            fullName: validUser.fullName,
            email: validUser.email,
          },
          (process.env.JWT_SECRET || "secret"),
          {
            expiresIn: '48h',
          })
          res.status(200).send({
            msg: "login-success",
            token: accessToken,
            data: validUser,
          });
      } else {
        res.status(404).send({ msg: "Invalid Credentials" });
      }
    }
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

router.get("/users", isAuth, async (req, res) => {
  try {
    const users = await User.find();
    if (users) {
      res.status(200).send({
        msg: "data found",
        count: users.length,
        data: users,
      });
    } else {
      res.status(404).send({ message: "User Not Found" });
    }
    
  } catch (error) {
    res.status(400).send({ message: error.message });    
  }
});

router.put("/:id",isAuth, async (req, res) => {
  try {
    const {fullName, email} = req.body;
    const userId = req.params.id;
    const user = await User.findById(userId);
    if (user) {
      user.fullName = fullName || user.fullName;
      user.email = email || user.email;
      const updatedUser = await user.save();
      res.status(200).send({
        msg: "user updated successfully",
        data: updatedUser,
      });
    } else {
      res.status(404).send({ message: "User Not Found" });
    }
    
  } catch (error) {
    res.status(400).send({ message: error.message });    
  }
});

router.get("/:id", isAuth, async (req, res) => {
  try {
    const userId = req.params.id;
    const user = await User.findById(userId);
    if (user) {
      res.status(200).send({
        msg: "data fetched successfully",
        data: user,
      });
    } else {
      res.status(404).send({ message: "User Not Found" });
    }
    
  } catch (error) {
    res.status(400).send({ message: error.message });    
  }
});

router.delete("/:id", isAuth, async (req, res) => {

  try {
    const userId = req.params.id;
    const user = await User.findByIdAndDelete(userId);
    if (user) {
      res.status(200).send({
        msg: "User deleted successfully",
      });
    } else {
      res.status(404).send({ message: "User Not Found" });
    }
    
  } catch (error) {
    res.status(400).send({ message: error.message });    
  }
});

module.exports = router;