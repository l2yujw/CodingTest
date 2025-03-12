-- 코드를 입력하세요
-- 자동차 종류(세단, suv), 2022-11-01~2022-11-30 대여가능
-- => end_date < 11-01, start_date > 11-30
-- 50 <= 30일간의 대여금액 < 200
-- => id, 종류, 대여금액(fee, 내림(같 차종(오, 같(id, 내림))
WITH p AS (
    SELECT car_type, discount_rate
    FROM car_rental_company_discount_plan
    WHERE car_type IN ('세단', 'SUV') 
        AND duration_type = '30일 이상'
), h AS (
    SELECT DISTINCT car_id
    FROM car_rental_company_rental_history
    WHERE start_date <= '2022-11-30' AND end_date >= '2022-11-01'
), c AS (
    SELECT car_id, car_type, daily_fee
    FROM car_rental_company_car
    WHERE car_id NOT IN (SELECT car_id FROM h)
), cp AS (
    SELECT c.car_id, c.car_type, ROUND((100 - p.discount_rate) * 0.01 * c.daily_fee * 30) AS fee
    FROM c
    JOIN p ON c.car_type = p.car_type
)

SELECT car_id, car_type, fee
FROM cp
WHERE fee >= 500000 AND fee < 2000000
ORDER BY fee DESC, car_type, car_id DESC