-- 코드를 입력하세요
-- user_info 가입한 회원 정보, online_sale 온라인 판매 상품정보
-- gender(0: 남자, 1:여자)
-- 동일 날짜, 회원ID, 상품ID조합 하나만 존재
-- 2021에 가입한 회원, 상품 구매 회원수, 상품 구매 회원 비율(2021년 구매 회원 수 / 2021년 전체 가입 회원 수) (소수 첫까지)
-- 년 오름 같다면 월 오름
SET @total_users := (SELECT count(*) FROM user_info WHERE year(joined) = 2021);

SELECT s.year, s.month, count(distinct s.user_id) as purchased_users, 
    round(count(distinct s.user_id) / @total_users, 1) AS purchased_ratio
FROM user_info i
JOIN (SELECT user_id, year(sales_date) AS year, month(sales_date) AS month
      FROM online_sale) s ON i.user_id = s.user_id
WHERE year(i.joined) = 2021
GROUP BY year, month
ORDER BY year, month