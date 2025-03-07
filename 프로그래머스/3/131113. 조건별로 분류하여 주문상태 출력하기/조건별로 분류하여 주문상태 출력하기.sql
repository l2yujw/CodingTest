-- 코드를 입력하세요
-- food_order 주문 정보
-- 22년 5월 1일 기준 => 주문id, 제품id, 출고자, 출고여부
-- 출고여부 (22년 5월 1일 <=) -> 출고완료, (이후 >) 출고대기, (미정) 출고미정
-- 주문id 오름차군
SELECT      order_id, product_id, date_format(out_date, '%Y-%m-%d') as out_date, 
        CASE 
            WHEN out_date <= '2022-05-01' THEN "출고완료"
            WHEN out_date > '2022-05-01' THEN "출고대기"
            ELSE "출고미정"
        END as "출고여부"
FROM        food_order
ORDER BY    order_id