-- 코드를 입력하세요
-- 생산일자 2022-05, 총매출(내림 (같으면 id(오름)))
SELECT p.product_id, p.product_name, p.price * o.amount AS total_sales
FROM food_product p
JOIN (SELECT product_id, SUM(amount) as amount
      FROM food_order
      WHERE produce_date LIKE '2022-05%'
      GROUP BY product_id) as o
ON p.product_id=o.product_id
ORDER BY total_sales desc, p.product_id