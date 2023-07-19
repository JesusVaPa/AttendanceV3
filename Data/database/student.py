from data.database.DataBase import *

class Student:
    def __init__(self, fname, lname, email):
        self.first_name = fname
        self.last_name = lname
        self.email = email

#Students
    def getStudents():
        query = "select * from Students;"
        cursor = cnx.cursor()
        cursor.execute(query)
        names = cursor.fetchall()
        cursor.close()
        #cnx.close()
        return names
    
    def getStudentByID(id):
        query = f"select * from Students where id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        name = cursor.fetchall()
        cursor.close()
        #cnx.close()
        return name
    
    #create a new student
    def postStudent(student):
        query = f"insert into Students(first_name, last_name, email) values ('{student.first_name}','{student.last_name}', '{student.email}');"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        id = cursor.lastrowid
        newStudent = Student.getStudentByID(id)
        cursor.close()
        #cnx.close()
        return newStudent
    
    def updateStudent(student, id):
        query = f"UPDATE Students SET first_name ='{student.first_name}', last_name = '{student.last_name}', email = '{student.email}' where id='{id}';"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        newStudent = Student.getStudentByID(id)
        cursor.close()
        #cnx.close()
        return newStudent
    
    def deleteStudent(id):
        query = f"DELETE FROM Students WHERE id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        #cnx.close()
        return True
   