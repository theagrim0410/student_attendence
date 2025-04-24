# Student Attendance Management System

This is a smart and interactive Student Attendance Manager that uses QR code scanning via webcam to mark students' **IN** and **OUT** attendance. It features:

-  Real-time webcam QR code scanning
-  Visual attendance graph (Pie chart)
-  Login portal for students and teachers
-  Individual and overall attendance tracking
-  Voice assistant for attendance summaries
-  MySQL-based backend for secure storage

---

##  Features

###  Real-Time Attendance via QR
- Students scan their ID card with the QR code
- IN and OUT attendance is recorded with timestamp
- Wrong entries or unknown IDs are logged separately

###  User Login Portal
- Students can log in with their name and admission number
- Teachers/admins can access all student attendance records

###  Attendance Graph
- Students get a visual pie chart showing attendance vs absences
- Graphs are dynamically generated using Matplotlib

###  Voice Assistant
- Attendance info is spoken aloud after login
- Feedback on errors like “student not found” is also spoken

---

##  Tech Stack

- **Frontend**: HTML, CSS 
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Computer Vision**: OpenCV + QRCodeDetector
- **Speech Engine**: pyttsx3
- **Data Visualization**: Matplotlib

---

---

##  How to Run

### Prerequisites
- Python 3.x
- MySQL server running with a database named `attendence_manager`  you can change the database and the tables accordingly
- Required Python packages

```
pip install flask opencv-python pyttsx3 matplotlib mysql-connector-python
```

## running command 
```
python main.py
