-- 코드를 입력하세요
-- Book 판매중 도서 정보, book_sales 각 도서의 날짜별 판매량 정보
-- 22년 1월, 카테고리별 (도서판매량 합산) => 카테고리, 총판매량
-- 카테고리명 오름차순
SELECT      b.category as "CATEGORY", sum(bs.sales) as "TOTAL_SALES"
FROM        book b JOIN book_sales bs ON b.book_id = bs.book_id
WHERE       date_format(bs.sales_date, '%Y-%m') = '2022-01'
GROUP BY    b.category
ORDER BY    b.category