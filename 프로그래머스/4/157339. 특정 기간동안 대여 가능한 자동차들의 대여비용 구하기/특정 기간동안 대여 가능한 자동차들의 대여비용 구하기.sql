WITH available_cars AS (
    SELECT c.car_id, c.car_type, c.daily_fee, p.discount_rate
    FROM car_rental_company_car c
    JOIN car_rental_company_discount_plan p 
        ON c.car_type = p.car_type
    LEFT JOIN car_rental_company_rental_history h
        ON c.car_id = h.car_id 
        AND h.start_date <= '2022-11-30' AND h.end_date >= '2022-11-01'
    WHERE p.duration_type = '30일 이상'
        AND c.car_type IN ('세단', 'SUV')
        AND h.car_id IS NULL  -- 대여 이력 없는 차량만
)

SELECT 
    car_id, 
    car_type, 
    FLOOR((100 - discount_rate) * 0.01 * daily_fee * 30) AS fee
FROM available_cars
WHERE (100 - discount_rate) * 0.01 * daily_fee * 30 BETWEEN 500000 AND 1999999
ORDER BY fee DESC, car_type, car_id DESC