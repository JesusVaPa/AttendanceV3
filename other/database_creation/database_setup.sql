use attendance;

create table Students(
	id int AUTO_INCREMENT not null Primary key,
	Last_Name varchar(50) not null,
	First_Name varchar(50) not null,
	Email varchar(50) not null
);

--select * from Students;