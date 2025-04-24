import mysql.connector
from datetime import datetime

# Reusable function to connect to database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", #add your host
        user="root", #add your username
        password="", #add your pass
        database="attendence_manager"  #add your database name
    )

# you must change the table name according to you
def store_attendence(admission, roll_no, student_name, classes):
    try:
        db = get_db_connection()
        cursor = db.cursor()

        now = datetime.now()
        date, time = now.date(), now.time()

        cursor.execute(
            "SELECT 1 FROM attendance_in WHERE addmision_no = %s AND date = %s LIMIT 1",
            (admission, date)
        )
        result = cursor.fetchone()

        if not result:
            cursor.execute(
                """
                INSERT INTO attendance_in (roll_no, student_name, date, classes, in_time, addmision_no)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (roll_no, student_name, date, classes, time, admission)
            )
            db.commit()
            print("✅ Attendance IN recorded successfully!")
        else:
            print("⚠️ You have already entered today.")

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

    finally:
        cursor.close()
        db.close()

def store_wrong(admission, entry_or_exit, reason):
    try:
        db = get_db_connection()
        cursor = db.cursor()

        now = datetime.now()
        date, time = now.date(), now.time()

        cursor.execute(
            """
            INSERT INTO attendence_fail (date, time, reason, entry_or_exit, addmision_no)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (date, time, reason, entry_or_exit, admission)
        )
        db.commit()
        print("🚫 Student not found! Error recorded.")

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

    finally:
        cursor.close()
        db.close()

def store_attendence_out(admission, roll_no, student_name, classes):
    try:
        db = get_db_connection()
        cursor = db.cursor()

        now = datetime.now()
        date, time = now.date(), now.time()

        cursor.execute(
            "SELECT 1 FROM attendance_in WHERE addmision_no = %s AND date = %s LIMIT 1",
            (admission, date)
        )
        result = cursor.fetchone()

        if result:
            cursor.execute(
                """
                INSERT INTO attendence_out (student_name, date, class, out_time, addmision_no, roll_no)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (student_name, date, classes, time, admission, roll_no)
            )
            db.commit()
            print("✅ Attendance OUT recorded successfully!")
        else:
            print("⚠️ Cannot checkout without checking in first!")

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

    finally:
        cursor.close()
        db.close()


