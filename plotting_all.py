import matplotlib.pyplot as plt
from datetime import datetime
import mysql.connector
import main

def get():
        db_connection = mysql.connector.connect(
        host="localhost", #add your own host
        user="root", # add your usrername
        password="", # add your pass
        database="attendence_manager"  # add your own database
    )
# you must change the table name according to you
        cursor = db_connection.cursor()
        cursor.execute("SELECT student_name, COUNT(*) as count FROM attendance_in GROUP BY student_name")
        results = cursor.fetchall()

        name_list = [row[0] for row in results]
        count_list = [row[1] for row in results]
        
        plot_all(name_list,count_list)
        
        
def plot_all(name,count):
   date1 = datetime(2025, 4, 1)  
   date2 = datetime.now()  
   delta = date2 - date1
   total = delta.days  
   main.speak("teacher")
   main.speak("Here is the graphical representation of all the students")
   plt.bar(name, count, color='skyblue', edgecolor='black')
   plt.title('Attendance Count')
   plt.xlabel('Names')
   plt.ylabel('Counts')
   for i in range(len(name)):
       perc = round((count[i]/total)*100,2)
       plt.text(i, count[i]/2, str(perc) + "%", ha='center', va='bottom', fontsize=12)
   plt.show()

# get()
    
        
        