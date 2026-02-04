-- 코드를 입력하세요
-- user_info 회원 정보, online_sale 온라인 판매 정보
-- gender 0(M) or 1(W)
-- 동일한 날짜, 회원id, 상품id 에 대해선 하나의 판매 데이터만 존재
-- (년, 월, 성별(없으면 제외))별로(오름), 상품 구매한 회원수
SELECT s.year, s.month, i.gender, count(distinct i.user_id) as users
FROM user_info i
JOIN (SELECT year(sales_date) AS year, month(sales_date) AS month, user_id
      FROM online_sale) as s ON i.user_id = s.user_id
WHERE i.gender IS NOT NULL
GROUP BY s.year, s.month, i.gender
ORDER BY s.year, s.month, i.gender