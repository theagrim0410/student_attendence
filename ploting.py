import matplotlib.pyplot as plt
from datetime import datetime
import mysql.connector
import main

def plot(admission):
    date1 = datetime(2025, 4, 1) 
    date2 = datetime.now()      
    delta = date2 - date1
    total = delta.days
    db_connection = mysql.connector.connect(
        host="localhost", #add your host
        user="root", #add your username
        password="", #add your pass
        database="attendence_manager" # add your database
    )
# you must change the table name according to you
    cursor = db_connection.cursor()
   
    query = """
        SELECT COUNT(*)
        FROM attendance_in
        WHERE addmision_no = %s
    """
    cursor.execute(query, (admission,))
    presents = cursor.fetchone()[0]
        
    if presents > total or presents == 0:
        # print("Wrong Attendance")
        main.speak(" Attendance did not Found ")
        
    else:
        # print(f"{admission} have attended {presents} classes out of {total}")
        main.speak(f"You have attended {presents} classes out of {total}")
        main.speak("Here is your attendance Graph")
        absents = total - presents
        values = [presents, absents]
        labels = ["PRESENT", "ABSENT"]
        # plt.figure(figsize=(6,6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'red'])
        plt.title(f'Attendance Graph for {admission}')
        plt.show()

# plot('23GCEBCS238')
