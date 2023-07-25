from database.DataBase import *

class Course_Model:
    def __init__(self, course_name):
        self.course_name = course_name

    def main() -> None:
        print('')

    def getCourses():
        query = "select * from Courses;"
        cursor = cnx.cursor()
        cursor.execute(query)
        courses = cursor.fetchall()
        cursor.close()
        #cnx.close()
        return courses

if __name__ == "__main__":
    main()