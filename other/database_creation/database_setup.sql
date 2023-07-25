use attendance;

create table Students(
	id int AUTO_INCREMENT not null Primary key,
	Last_Name varchar(50) not null,
	First_Name varchar(50) not null,
	Email varchar(50) not null
);

--select * from Students;

CREATE table Courses(
	id int AUTO_INCREMENT not null Primary key,
	Course_Name varchar(50) not null,
)

create table Classes_Attendance(
	id int AUTO_INCREMENT not null Primary key,
	Student_ID int,
	Course_ID Int,
	Class_Date datetime,
	FOREIGN KEY (Student_ID) REFERENCES Students(id)
	FOREIGN KEY (Course_ID) REFERENCES Courses(id)
)
