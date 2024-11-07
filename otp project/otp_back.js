const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());


const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Taranjot2008',
    database: 'otp_data',
    port: 3306
});

db.connect((err) => {
    if (err) {
    console.error('Database connection failed:', err.stack);
    return;
    }
    console.log(`Connected to MySQL database`);
});

  // Handle data from fetch request
app.post('/submit', (req, res) => {
    const { otp_string } = req.body;
    const query = 'INSERT INTO otp_d (otp) VALUES (?, ?)';

    db.query(query, [otp], (err, results) => {
    if (err) {
        console.error('Error inserting data:', err);
        return res.status(500).send('Server error');
    }
    res.status(200).send('Data inserted successfully');
    });
});

  // Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});