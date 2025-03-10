-- 코드를 입력하세요
-- 식품분류별, 제일 비싼 => 분류, 가격(내림), 이름
-- 분류 (과자,국,김치,식용유)
SELECT category, price as max_price, product_name
FROM food_product
WHERE (category, price) IN (SELECT category, max(price)
                            FROM food_product
                            WHERE category IN ('과자', '국', '김치', '식용유')
                            GROUP BY category)
ORDER BY price desc