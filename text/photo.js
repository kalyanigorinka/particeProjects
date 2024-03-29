const multer = require('multer');
const path = require('path');
const router = require("express").Router();


const imageStorage = multer.diskStorage({
  // Destination to store image     
  destination: 'images',
  filename: (req, file, cb) => {
    cb(null, file.fieldname + '_' + Date.now()+'_'
      + path.extname(file.originalname))
    // file.fieldname is name of the field (image)
    // path.extname get the uploaded file extension
  }
});

const imageUpload = multer({
  storage: imageStorage,
  limits: {
    fileSize: 1000000 // 1000000 Bytes = 1 MB
  },
  fileFilter (req, file, cb) {
    if (!file.originalname.match(/\.(png|jpg)$/)) {
      // upload only png and jpg format
      return cb(new Error('Please upload a Image'))
    }
    cb(undefined, true)
  }
})

// For Single image upload
router.post('/uploadImage', imageUpload.single('image'), (req, res) => {
  res.send(req.file)
}, (error, res) => {
  res.status(400).send({ error: error.message })
})

// For multiple image upload

router.post('/uploadBulkImage', imageUpload.array('images', 4), (req, res) => {
  res.send(req.files)
}, (error, res) => {
  res.status(400).send({ error: error.message })
})

//for video upload

const videoStorage = multer.diskStorage({
  destination: 'videos', // Destination to store video 
  filename: (req, file, cb) => {
    cb(null, file.fieldname + '_' + Date.now()
      + path.extname(file.originalname))
  }
});

const videoUpload = multer({
  storage: videoStorage,
  limits: {
    fileSize: 10000000 // 10000000 Bytes = 10 MB
  },
  fileFilter (req, file, cb) {
    // upload only mp4 and mkv format
    if (!file.originalname.match(/\.(mp4|MPEG-4|mkv)$/)) {
      return cb(new Error('Please upload a video'))
    }
    cb(undefined, true)
  }
})

router.post('/uploadVideo', videoUpload.single('video'), (req, res) => {
  res.send(req.file)
}, (error, req, res, next) => {
  res.status(400).send({ error: error.message })
})

module.exports = router;