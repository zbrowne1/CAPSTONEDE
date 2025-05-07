
-- 1️⃣ Top 5 Best-Selling Products by Revenue
SELECT 
    product_name, 
    SUM(total_price) AS total_revenue
FROM order_items
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 5;

-- 2️⃣ Total Sales by Region
SELECT 
    c.region,
    SUM(o.total_amount) AS total_sales
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.region
ORDER BY total_sales DESC;
