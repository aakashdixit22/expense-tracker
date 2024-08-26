const mongoose= require('mongoose');    
// schema design creating
const userSchema = new mongoose.Schema({
    name:{
        type:String,
        required:[true,'Please provide a name'],

    },
    email:{
        type:String,
        required:[true,'Please provide a email'],
        unique:true,
    },
    password:{
        type:String,
        required:[true,'Please provide a password'],
    },  
},{timestamps:true});//timestamps:true is used to create the time of creation and updation

//export
const userModel= mongoose.model('users',userSchema);
module.exports=userModel;