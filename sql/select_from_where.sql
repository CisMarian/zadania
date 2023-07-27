1. 
SELECT *
FROM Customers AS c 
WHERE c.Country="USA" AND c.Age>30;

2.
SELECT *
FROM Customers AS c
WHERE c.Country="Canada" AND c.Age=25;

3.
SELECT *
FROM Customers AS c 
WHERE c.Country="Canada" AND c.Name LIKE "%a";

4. 
SELECT *
FROM Customers AS c 
WHERE c.Country IN ("Canada", "USA", "UK");

5.
SELECT *
FROM Customers AS c 
WHERE c.Country="USA";

6. 
SELECT c.Name, c.Age
FROM Customers AS c 
WHERE c.ID=3;

7. 
SELECT *
FROM Customers AS c 
WHERE c.Age>40;

8.
SELECT *
FROM Customers AS c 
WHERE c.Country="USA" AND c.Age BETWEEN 30 and 40;

9.
SELECT *
FROM Customers AS c 
WHERE c.Name LIKE "E%;"