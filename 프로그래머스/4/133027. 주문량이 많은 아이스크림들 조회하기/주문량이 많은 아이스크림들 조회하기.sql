-- 코드를 입력하세요
-- first_half 상반기 주문정보
-- july 7월 주문정보
-- 7월 아이스크림 총주문량 + 상반기 총 주문량 이 큰 순서대로
SELECT h.flavor
FROM first_half h
JOIN (SELECT flavor, sum(total_order) as total_order
      FROM JULY
      GROUP BY flavor) j ON h.flavor = j.flavor
ORDER BY (h.total_order + j.total_order) desc
LIMIT 3