-- 코드를 입력하세요
-- car_rental_company_rental_history 자동차 대여 기록 정보
-- 2022-10-16 >= end date 이면 대여중, 아니면 대여가능 표시(availability)
SELECT car_id, 
    CASE
        WHEN car_id IN (SELECT car_id
                FROM car_rental_company_rental_history
                WHERE '2022-10-16' BETWEEN start_date AND end_date) THEN '대여중'
        ELSE '대여 가능'
    END as availability
FROM car_rental_company_rental_history
GROUP BY car_id
ORDER BY car_id desc