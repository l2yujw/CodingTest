-- 코드를 입력하세요
-- cart_products 장바구니에 담긴 상품 정보
-- 우유&요거트 동시 구입 장바구니가 있는지 => 장바구니Id순
SELECT CART_ID
  FROM CART_PRODUCTS
 WHERE NAME IN ('Milk','Yogurt')
 GROUP BY CART_ID
 HAVING COUNT(DISTINCT NAME)=2