-- 코드를 입력하세요
-- 대여 자동차 정보 car_rental_company_car
-- 대여 기록 car_rental_company_rental_history
-- 차종별 대여기간 종류별 할인 정책 정보 car_rental_company_discount_plan
-- 차종(세단, suv, 승합차, 트럭, 리무진)
-- 옵션 ,로 구분
-- 키워드 종류(주차감지센서, 스마트키, 네비게이션, 통풍시트, 열선시트, 후방카메라, 가죽시트)
-- 대여기간(7일이상, 30일이상, 90일이상) => 7일미만 할인 정책x
-- 차종 트럭, 대여 기록별, 대여금액(fee, 정수부분만) => 대여기록id, 대여금액(내림, 같 기록id(내림)
# SELECT h.history_id, ROUND(((100 - IFNULL(max(p.duration_type) , 0)) * 0.01) * h.daily_fee * h.duration ) as fee
# FROM (SELECT h.history_id, h.car_id, DATEDIFF(h.end_date, h.start_date) + 1 as duration, 
#         c.daily_fee, c.car_type
#       FROM car_rental_company_rental_history h
#       JOIN car_rental_company_car c ON h.car_id = c.car_id
#       WHERE c.car_type = '트럭') as h
# LEFT JOIN (SELECT CAST(REPLACE(p.duration_type, '일 이상', '') as unsigned) as duration_type, p.discount_rate, p.car_type
#            FROM car_rental_company_discount_plan p
#            WHERE p.car_type = '트럭') as p
#       ON h.duration >= p.duration_type
# GROUP BY h.history_id
# ORDER BY fee desc, h.history_id desc


# SELECT *
# FROM (SELECT h.history_id, h.car_id, DATEDIFF(h.end_date, h.start_date) + 1 as duration, 
#         c.daily_fee, c.car_type
#       FROM car_rental_company_rental_history h
#       JOIN car_rental_company_car c ON h.car_id = c.car_id
#       WHERE c.car_type = '트럭') as h
# LEFT JOIN (SELECT CAST(REPLACE(p.duration_type, '일 이상', '') as unsigned) as duration_type, 
#                 p.discount_rate, p.car_type
#            FROM car_rental_company_discount_plan p
#            WHERE p.car_type = '트럭') as p
#       ON h.duration >= p.duration_type
# GROUP BY h.history_id


SELECT h.history_id ,
ROUND(((100 - IFNULL(max(p.discount_rate), 0)) * 0.01) * c.daily_fee * (DATEDIFF(h.end_date, h.start_date) + 1)) as fee
FROM car_rental_company_rental_history h
JOIN car_rental_company_car c ON h.car_id = c.car_id
LEFT JOIN (SELECT CAST(REPLACE(p.duration_type, '일 이상', '') as unsigned) as duration_type, p.discount_rate, p.car_type
           FROM car_rental_company_discount_plan p
           WHERE p.car_type = '트럭') as p
      ON DATEDIFF(h.end_date, h.start_date) + 1 >= p.duration_type
WHERE c.car_type = '트럭'
GROUP BY h.history_id
ORDER BY fee desc, h.history_id desc
