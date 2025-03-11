-- 코드를 입력하세요
-- online_sale, offline_sale
-- 동일한 날짜, 상품id 조합은 중복x
-- 2022-03의 온오프 판매데이터 => 판매 날짜(오름, 같다면 상품id_(오름, 같다면(유저id)), 상품id, 유저id, 판매량
-- offline_sale의 userId는 null
SELECT DATE_FORMAT(SALES_DATE,"%Y-%m-%d") SALES_DATE,
    PRODUCT_ID,
    USER_ID,
    SALES_AMOUNT
FROM ONLINE_SALE
WHERE sales_date >= '2022-03-01' and sales_date < '2022-04-01'

UNION ALL

SELECT DATE_FORMAT(SALES_DATE,"%Y-%m-%d") SALES_DATE,
    PRODUCT_ID,
    NULL AS USER_ID,
    SALES_AMOUNT
FROM OFFLINE_SALE 
WHERE sales_date >= '2022-03-01' and sales_date < '2022-04-01'
    
ORDER BY SALES_DATE , PRODUCT_ID , USER_ID