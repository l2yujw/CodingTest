-- 코드를 입력하세요
-- used_goods_board 게시판 정보
-- used_goods_user 게시판 사용자 정보
-- 완료된, 총금액 70만이상 => 회원id, 닉네임, 총거래금액(오름차순)
SELECT uu.user_id, uu.nickname, sum(ub.price) as TOTAL_SALES
FROM used_goods_board ub
JOIN used_goods_user uu ON ub.writer_id = uu.user_id
WHERE ub.status = 'DONE'
GROUP BY ub.writer_id
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES