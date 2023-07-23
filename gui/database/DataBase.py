import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!Priscilla1",
    database="attendance",
    port=3310
)

# class DataBase:
# #Professors
#     def getProfessors():
#         query = "select * from Professors;"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         names = cursor.fetchall()
#         cnx.close()
#         return names
    
#     def getProfessorByID(id):
#         query = f"select * from Professors where id={id};"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         name = cursor.fetchall()
#         cnx.close()
#         return name
#     #create a new professor
#     def postProfessor(professor):
#         query = f"insert into Professors(Name) values ('{professor.Name}');"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         cnx.commit()
#         id = cursor.lastrowid
#         newProfessor = DataBase.getProfessorByID(id)
#         cnx.close()
#         return newProfessor
    
#     def updateProfessor(professor, id):
#         query = f"UPDATE Professors SET NAME ='{professor.Name}' where id='{id}';"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         cnx.commit()
#         newProfessor = DataBase.getProfessorByID(id)
#         cursor.close()
#         cnx.close()
#         return newProfessor
    
#     def deleteProfessor(id):
#         query = f"DELETE FROM Professors WHERE id={id};"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         cnx.commit()
#         cursor.close()
#         cnx.close()
#         return True

 
# #Courses
#     def getCourses():
#         query = "select * from Courses;"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         courses = cursor.fetchall()
#         cnx.close()
#         return courses
    
#     def getCourseByID(id):
#         query = f"select * from Courses where id={id};"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         course = cursor.fetchall()
#         cnx.close()
#         return course
#     #create a new course
#     def postCourse(course):
#         query = f"insert into Courses(Name) values ('{course.Name}');"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         cnx.commit()
#         id = cursor.lastrowid
#         newCourse = DataBase.getCourseByID(id)
#         cnx.close()
#         return newCourse
    
#     def updateCourse(course, id):
#         query = f"UPDATE Courses SET NAME ='{course.Name}' where id='{id}';"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         cnx.commit()
#         newCourse = DataBase.getCourseByID(id)
#         cursor.close()
#         cnx.close()
#         return newCourse
    
#     def deleteCourse(id):
#         query = f"DELETE FROM Courses WHERE id={id};"
#         cursor = cnx.cursor()
#         cursor.execute(query)
#         cnx.commit()
#         cursor.close()
#         cnx.close()
#         return True
