1. 
SELECT o.customer_id, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o 
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 10;

2.
SELECT o.customer_id, SUM(o.total_amount) AS sum_of_orders, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o
GROUP BY customer_id
HAVING COUNT(o.order_id) > 10;

3.
SELECT o.customer_id, SUM(o.total_amount) AS max_of_all_orders, COUNT(o.order_id) AS no_of_orders
FROM Orders as o
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 10
ORDER BY SUM(o.total_amount) DESC
LIMIT 1;

4.
SELECT o.customer_id, EXTRACT(MONTH FROM o.order_date) AS MONTH, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o
GROUP BY o.customer_id, EXTRACT(MONTH FROM o.order_date)
HAVING COUNT(o.order_id) > 10;

5.
SELECT o.customer_id, AVG(o.total_amount), COUNT(o.order_id) AS no_of_orders
FROM Orders AS o 
GROUP BY customer_id
HAVING COUNT(o.order_id) > 10;

6.
SELECT o.order_date, MAX(o.total_amount) AS max_order, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o
GROUP BY o.order_date
HAVING COUNT(o.order_id) > 10
ORDER BY MAX(o.total_amount) DESC
LIMIT 1;

7.
SELECT p.category_id, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o 
JOIN OrderDetails AS od ON o.order_id=od.order_id
JOIN Products AS p ON od.product_id=p.product_id
GROUP BY p.category_id
HAVING COUNT(o.order_id) > 10;

8.
SELECT o.customer_id, COUNT(o.order_id) AS no_of_orders
FROM Orders AS od
GROUP BY o.customer_id
HAVING COUNT(o.order_id) >= 3;

9.
SELECT p.category_id, SUM(o.total_amount) AS sum_of_orders, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o 
JOIN OrderDetails AS od ON o.order_id=od.order_id
JOIN Products AS p ON od.product_id=p.product_id
GROUP BY p.category_id
HAVING COUNT(o.order_id) AS no_of_orders > 10;

10.
SELECT o.customer_id, COUNT(o.order_id) AS no_of_orders
FROM Orders AS o 
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 10
ORDER BY COUNT(o.order_id) DESC
LIMIT 1;