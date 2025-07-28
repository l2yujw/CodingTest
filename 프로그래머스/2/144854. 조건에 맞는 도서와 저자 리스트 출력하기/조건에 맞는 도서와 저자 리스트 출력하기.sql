-- 코드를 입력하세요
SELECT b.book_id, a.author_name, date_format(b.published_date, '%Y-%m-%d')
FROM book b, author a
WHERE b.author_id = a.author_id AND category LIKE '경제'
ORDER BY b.published_date