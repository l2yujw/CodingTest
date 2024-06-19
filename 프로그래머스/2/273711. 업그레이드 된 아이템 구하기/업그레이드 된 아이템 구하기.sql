-- 코드를 작성해주세요
select  i.item_id, i.item_name, i.rarity
from    item_tree t, item_info i
where   t.item_id = i.item_id and
        parent_item_id in (
                select  item_id
                from    item_info
                where   rarity = "rare"
        )
order by    i.item_id desc
