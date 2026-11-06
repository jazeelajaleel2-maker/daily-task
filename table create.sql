use [STUDENTDB];
select * from [dbo].[cardata (1)] ;
select * from [dbo].[cardata (1)] where year > 2015 ;
select * from[dbo].[cardata (1)] where fuel_type='Petrol';
select DISTINCT fuel_type from [dbo].[cardata (1)] ;
select DISTINCT * from [dbo].[cardata (1)] ;
select count (Car_name) from [dbo].[cardata (1)]
select * from [dbo].[cardata (1)] where car_name = 'innova' ;

select * from [dbo].[cardata (1)]where kms_driven > 1000;
select * from [dbo].[cardata (1)]where Year BETWEEN 2000AND 2010;
select * from [dbo].[cardata (1)]where Fuel_Type IN ('Petrol','Diesel');




CREATE TABLE Customers(
customerID INT PRIMARY KEY identity(100,1),
customerName VARCHAR(100) NOT NULL,
ContactName VARCHAR(100),
Address VARCHAR(255),
City VARCHAR(50),
PostalCode CHAR(6),
Country VARCHAR(50),
Email VARCHAR(100) UNIQUE,
JoinDate DATE DEFAULT getdate(),
);

select * from [dbo].[Customers];