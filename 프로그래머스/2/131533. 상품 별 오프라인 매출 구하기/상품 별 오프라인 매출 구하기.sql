-- 코드를 입력하세요
SELECT  p.product_code, (p.price * SUM(o.sales_amount)) AS 'sales'
FROM    product p, offline_sale o
WHERE   p.product_id = o.product_id
GROUP BY    p.product_code
ORDER BY    sales DESC, product_code