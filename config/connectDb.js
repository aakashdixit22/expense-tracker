const mongoose = require('mongoose');
const colors=require('colors');
require('dotenv').config();
const connectDb = async () => {
    try{
        await mongoose.connect(process.env.MONGO_URL)
        console.log(`server running on the ${mongoose.connection.host}`.bgCyan.white);
    }catch(err){    
        console.log(`Error: ${err.message}`.bgRed);
    }
}
module.exports = connectDb;