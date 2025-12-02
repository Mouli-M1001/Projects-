create schema revise_stored_func;
use revise_stored_func;

--  -------- What is a Stored Function? (Simple Meaning) ---------------
-- A Stored Function is a small program saved inside the database that:
--  accepts input -->  performs calculations/operations  -->  returns a single value back
-- 		Reuse logic (write once, use many times)
-- 		Keep code clean (no repeated calculations in queries)
-- 		Return a value directly in SELECT queries 
-- Must always return a value using RETURN.
-- Can be used in SELECT, WHERE, ORDER BY, etc.
-- Cannot modify tables (MySQL restricts update/insert/delete inside functions).
-- Input is given using parameters (IN only).


-- ---------- syntax ------------
-- 	DELIMITER $$  
-- 	CREATE FUNCTION function_name (parameters)  
-- 	RETURNS datatype  
-- 	DETERMINISTIC  
-- 	BEGIN  
-- 	   -- logic  
-- 	RETURN value;
-- 	END $$  
-- 	DELIMITER ;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary INT,
    hire_date DATE,
    department VARCHAR(30));

INSERT INTO employees VALUES
(1, 'Rahul', 'Shah', 30000, '2018-05-10', 'Finance'),
(2, 'Anita', 'Rao', 45000, '2019-11-22', 'IT'),
(3, 'Vijay', 'Kumar', 38000, '2017-01-15', 'Sales'),
(4, 'Meena', 'Kaur', 52000, '2020-03-08', 'HR'),
(5, 'Arun', 'Nair', 28000, '2016-09-25', 'Logistics'),
(6, 'Sneha', 'Patel', 60000, '2015-08-19', 'IT'),
(7, 'Kiran', 'Das', 40000, '2021-02-14', 'Finance');
select *from employees;

-- Function 1 — Calculate Yearly Salary
delimiter $$
create function yearly_salary (total int)
returns int
deterministic
begin 
return total*12;
end $$
delimiter ;
select concat(first_name," ",last_name) as name , salary , yearly_salary(salary) from employees;

-- Function 2 — Get Full Name
delimiter $$
create function full_name (A varchar(10),B varchar(10))
returns varchar(25)
deterministic
begin 
return concat(A," ",B);
end $$
delimiter ;

select full_name(first_name,last_name) from employees;

-- Function 3 — Calculate Experience (in years)
delimiter $$
create function experience (hdate date)
returns int
deterministic
begin 
return  timestampdiff(year,hdate,curdate());
end $$
delimiter ;

select first_name, experience(hire_date) as Experience from employees;

-- To find total_days 

delimiter $$
create function days (hdate date)
returns int
deterministic
begin 
return  timestampdiff(day,hdate,curdate());
end $$
delimiter ;

select first_name, days(hire_date) as Experience from employees;

--  Function 4 — 10% Tax Amount

delimiter $$
create function taxes_10(X int)
returns int
deterministic
begin 
return  x*0.1;
end $$
delimiter ;

select first_name ,salary, taxes_10(salary) as to_deduct from employees; 

-- Function 5 — Increase Salary by Given Percentage 

delimiter $$
create function inc (X int , per int )
returns int
deterministic
begin 
return  x+(x*per/100);
end $$
delimiter ;

select first_name , salary , inc(salary,25) as increment from employees;
