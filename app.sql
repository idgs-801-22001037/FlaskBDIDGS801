CREATE DATABASE bdidgs801_2;

use bdidgs801_2;

/*
3 querys que metaan los sigioentes datos: id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apaterno = db.Column(db.String(100))
    email = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

*/
-- just insertINSERT INTO Alumnos VALUES (1,"Carlos","Padilla","carlos@gmail.com",CURDATE());
INSERT INTO Alumnos VALUES (1,"Pepe","Suárez","pepe@gmail.com",CURDATE());
INSERT INTO Alumnos VALUES (2,"Juan","López","juan@gmail.com",CURDATE());

show TABLES;