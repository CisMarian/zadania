1.
SELECT c.first_name, c.last_name, o.order_number
FROM Orders AS o
JOIN Customers as C ON o.customer_id=c.customer_id;

2. 
SELECT p.product_name, p.price, od.quantity
FROM Products AS p
JOIN OrderDetails AS od ON p.product_id=od.product_id;

3.
SELECT e.first_name, e.last_name, o.order_number
FROM Employees AS e
LEFT JOIN Orders AS o ON e.employee_id=o.employee_id;

4.
SELECT c.first_name, c.last_name, COUNT(o.order_number)
FROM Customers AS c 
JOIN Orders AS o ON c.customer_id=o.customer_id
GROUP BY c.first_name, c.last_name
ORDER BY COUNT(o.order_number) DESC;

5.
SELECT c.category_name, COUNT(p.product_id)
FROM Categories AS c
JOIN Products AS p ON c.category_id=p.category_id
GROUP BY c.category_name;

6.
SELECT c.first_name, c.last_name, o.order_number
FROM Customers AS c
LEFT JOIN Orders AS o ON c.customer_id=o.customer_id;

7.
SELECT e.first_name, e.last_name, c.first_name, c.last_name
FROM Emploees AS e
LEFT JOIN Customers AS c ON e.sales_rep_id=c.customer_id
WHERE e.sales_rep_id IS NOT null and e.sales_rep_id = 1;

8. 
SELECT o.order_number, p.product_name, od.quantity
FROM OrderDetails AS od
JOIN Orders AS o ON od.order_id=o.order_id
JOIN Products AS p ON od.product_id=o.product_id; 

9.
SELECT c.category_name, p.product_name
FROM Categories AS c
LEFT JOIN Products AS p ON c.category_id=p.category_id;

10.
SELECT c.first_name, c.last_name, SUM(od.quantity) AS order_value 
FROM Customers AS c
JOIN Orders AS o ON c.customer_id=o.customer_id 
JOIN OrderDetails AS od ON o.order_id=od.order_id 
GROUP BY c.first_name, c.last_name
ORDER BY SUM(od.quantity) DESC;

