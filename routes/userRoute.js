const express=require('express');
const {loginController,registerController}=require('../controllers/userController');

//routers
const router=express.Router();

// post and login '
router.post('/login',loginController)
//post register
router.post('/register',registerController)

module.exports=router;