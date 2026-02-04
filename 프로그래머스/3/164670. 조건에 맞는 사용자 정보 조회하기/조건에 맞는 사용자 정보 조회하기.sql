-- 코드를 입력하세요
-- used_goods_board 게시판 정보
-- used_goods_user 사용자 정보
-- 3건이상 사용자 => 사용자id(내림차순), 닉네임, 전체주소(시 + 도로명 주소, 상세주소), 전화번호(xxx-xxxx-xxxx)
SELECT u.user_id, u.nickname, concat(u.city, ' ', u.street_address1, ' ', u.street_address2) as 전체주소,
concat(substr(u.tlno, 1, 3), '-', substr(u.tlno, 4, 4), '-', substr(u.tlno, 8)) AS '전화번호'
FROM used_goods_user u
WHERE u.user_id IN (SELECT b.writer_id
                   FROM used_goods_board b
                   GROUP BY b.writer_id
                   HAVING count(*) >= 3)
ORDER BY u.user_id desc