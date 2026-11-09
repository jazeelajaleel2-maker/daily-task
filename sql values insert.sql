use STUDENTDB ;


CREATE TABLE STUDENTS(
Id INT Primary key identity(1,1),
StdName VARCHAR(100) NOT NULL,
Contactno CHAR(10),
Postalcode CHAR(6),
City varchar(100),
subs varchar(100),

);
select * from [dbo].[STUDENTS];

INSERT INTO [dbo].[STUDENTS](StdName,Contactno,Postalcode,City,subs)
VALUES('swalih',1234567890,673637,'vengara','chemistry')