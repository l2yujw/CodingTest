-- 코드를 입력하세요
-- rest_info 식당 정보, rest_review 리뷰 정보
-- 서울에 위치,
-- => id, 이름, 종류, 즐찾수, 평균점수(셋에서 반올림 = 둘까지)(내림, 같다면 즐찾수 (내림))
SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, r.score
FROM rest_info i
JOIN (SELECT rest_id, round(avg(review_score), 2) as score
      FROM rest_review
      GROUP BY rest_id) as r ON i.rest_id = r.rest_id
WHERE i.address LIKE "서울%"
ORDER BY r.score desc, i.favorites desc