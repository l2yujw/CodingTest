-- 코드를 입력하세요
-- CAR_RENTAL_COMPANY_CAR, 대여중인 자동차 정보
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY, 대여기록정보
-- 자동차 종류 = 세단, 10월에 대여시작 => 자동차ID리스트 (중복X, 내림차순)
SELECT      DISTINCT cr.car_id
FROM        car_rental_company_car cr
JOIN        car_rental_company_rental_history rh ON cr.car_id = rh.car_id
WHERE       cr.car_type = '세단' AND rh.start_date >= '2022-10-01'
ORDER BY    cr.car_id DESC