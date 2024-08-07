SELECT  i.animal_id, i.animal_type, i.name
FROM    animal_ins i
JOIN    animal_outs o on i.animal_id = o.animal_id
WHERE   i.sex_upon_intake like 'Intact%'
and (o.sex_upon_outcome like 'Spayed%' or o.sex_upon_outcome like 'Neutered%')
ORDER BY    i.animal_id