const express = require("express");
const { getAllTransection, addTransection,editTransection,deleteTransection } = require("../controllers/transectionCtrl");

//router object
const router = express.Router();

//routes
//add transection POST MEthod
router.post("/add-transection", addTransection);
//edit transection
router.post("/edit-transection", editTransection);
//delete transection
router.post("/delete-transection", deleteTransection);
//get transections
router.post("/get-transection", getAllTransection);

module.exports = router;