## -- Student Information Management System

This project is a CLI-based Student Information Management System built using Python and MySQL.  
It demonstrates backend fundamentals such as database design, CRUD operations, environment-based configuration, and clean project structuring.

The project was initially implemented as a file-based system and later migrated to a relational MySQL backend following real-world migration practices.

---

## -- Project Files

- **README.md** – Project overview and usage  
- **requirements.txt** – Python dependencies  
- **database/schema.sql** – SQL script to create database and tables  
- **src/** – Application source code  
- **legacy_file_version/** – Old file-based implementation  

---

## -- Features

- Student management (Create, Read, Update, Delete)  
- Subject management (Create, Read, Update, Delete)  
- Marks management linked to students and subjects  
- MySQL-backed persistent storage  
- Environment-based configuration using `.env`  
- Clean separation of CLI logic and database logic  
- Legacy file-based system preserved for reference  

---

## -- Tech Stack

- **Language:** Python 3  
- **Database:** MySQL  
- **DB Connector:** mysqlclient / MySQLdb  
- **Version Control:** Git & GitHub  
- **Environment Management:** python-dotenv  

---


## -- Database Schema Overview

### Tables Included

- students  
- subjects  
- marks  

### Relationships

- A student can have marks for multiple subjects  
- Each marks entry links one student to one subject  
- Foreign key constraints with cascading deletes  

---

---

## Migration Note
The legacy file-based implementation is preserved in the `legacy_file_version/` directory to demonstrate the migration process from flat-file storage to a relational **MySQL** database.

---

## Future Enhancements
* **Authentication & Roles:** Implementing secure login and role-based access control.
* **Input Validation:** Adding a robust validation layer for data integrity.
* **Performance Reports:** Generating automated student-wise performance analytics.
* **REST API:** Transitioning the system to a web-based architecture using **Flask** or **FastAPI**.

---

## Author
**Paul Raja** GitHub: [https://github.com/paul-raja-dev](https://github.com/paul-raja-dev)

---

## License
This project is for **educational use only**.


