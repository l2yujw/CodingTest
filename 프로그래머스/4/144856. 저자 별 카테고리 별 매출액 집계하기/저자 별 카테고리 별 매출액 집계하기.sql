-- 코드를 입력하세요
-- book 도서정보, author 저자정보, book_sales
-- 2022-01, 저자별, 카테고리별, 매출액(total_sales=판매량*판매가) as sales
-- 저자id(오름, 같다면 카테고리(내림))
SELECT a.author_id, a.author_name, b.category, sum(b.price * s.sales) AS total_sales
FROM book b
JOIN author a ON b.author_id = a.author_id
JOIN (SELECT book_id, SUM(sales) as sales
      FROM book_sales
      WHERE sales_date LIKE '2022-01%'
      GROUP BY book_id
      ) as s ON b.book_id = s.book_id
GROUP BY a.author_id, b.category
ORDER BY a.author_id, b.category desc