from database.DataBase import *

class Classes_Attendance_Model:
    def __init__(self, student_id, course_id, class_date):
        self.student_id = student_id
        self.course_id = course_id
        self.class_date = class_date

    def main() -> None:
        print('')
    
    def getClassAttendanceByID(id):
        query = f"select * from Classes_Attendance where id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        name = cursor.fetchall()
        cursor.close()
        #cnx.close()
        return name
    
    #create a new student
    def postClassAttendance(self):
        query = f"insert into Classes_Attendance(Student_ID, Course_ID, Class_Date) values ('{self.student_id}','{self.course_id}', '{self.class_date }');"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        id = cursor.lastrowid
        new_attedance_list = Classes_Attendance_Model.getClassAttendanceByID(id)
        cursor.close()
        #cnx.close()
        return new_attedance_list
    
if __name__ == "__main__":
    main()