/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-07 08:58:53
# @File    : SQL73-2.sql
# @Note    :
**************************************************************************************/

select g1.id, l.name, g1.score
from grade g1 
join language l on g1.language_id=l.id
where (
    select count(distinct g2.score)
    from grade g2
    where g2.score>=g1.score and g1.language_id=g2.language_id
)<=2 
order by l.name asc,g1.score desc ,g1.id asc;