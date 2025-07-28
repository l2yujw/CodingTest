-- 코드를 입력하세요
-- 대여 시작일 기준 2022-8~2022-10 총 대여 횟수가 5회이상
-- 월별 자동차 id별 총 대여 횟수 as records
WITH popular_cars AS (
    SELECT      car_id
    FROM        car_rental_company_rental_history
    WHERE       start_date >= '2022-08-01' AND start_date < '2022-11-01'
    GROUP BY    car_id
    HAVING      COUNT(*) >= 5
)

SELECT      MONTH(start_date) AS 'month', 
            car_id, 
            COUNT(*) AS 'records'
FROM        car_rental_company_rental_history
WHERE       start_date >= '2022-08-01' AND start_date < '2022-11-01' 
            AND car_id IN (SELECT car_id FROM popular_cars)
GROUP BY    month, car_id
ORDER BY    month, car_id DESC;