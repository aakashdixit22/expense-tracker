const express = require('express');
const app = express();
const port = process.env.PORT || 5000;
const cors = require('cors'); // Middleware
const morgan = require('morgan'); // Middleware
const dotenv = require('dotenv'); // Middleware
const colors = require('colors'); // Middleware
const connectDb = require('./config/connectDb'); // Middleware

// Load environment variables
dotenv.config();

// Connect to the database (only once)
connectDb();

// Middleware
app.use(cors());
app.use(morgan('dev'));
app.use(express.json());

// Routes for user
app.use('/api/v1/users', require('./routes/userRoute'));

// Transaction routes
app.use('/api/v1/transections', require("./routes/transectionRoutes"));

app.get('/', (req, res) => {
    res.send('Hello World!');
});
// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

