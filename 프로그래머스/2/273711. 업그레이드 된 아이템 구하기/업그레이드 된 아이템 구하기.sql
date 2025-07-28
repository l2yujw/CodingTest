-- 코드를 작성해주세요
WITH RareItems AS (
    SELECT item_id
    FROM item_info
    WHERE rarity = 'rare'
)
SELECT i.item_id, i.item_name, i.rarity
FROM item_tree t
JOIN item_info i ON t.item_id = i.item_id
JOIN RareItems r ON t.parent_item_id = r.item_id
ORDER BY i.item_id DESC;