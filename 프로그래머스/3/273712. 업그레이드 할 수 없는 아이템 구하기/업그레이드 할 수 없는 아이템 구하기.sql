-- 코드를 작성해주세요
-- item_a -> item_b 업글 a가 엄마
-- root의 parent null
-- 더이상 업글 불가 아이템
WITH leaf_items AS (
    SELECT i1.item_id
    FROM item_tree i1
    LEFT JOIN item_tree i2 ON i1.item_id = i2.parent_item_id
    WHERE i2.parent_item_id IS NULL
)

SELECT ii.item_id, ii.item_name, ii.rarity
FROM item_info ii
JOIN leaf_items li ON ii.item_id = li.item_id
ORDER BY ii.item_id DESC;