/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-09 08:51:56
# @File    : Q76.sql
# @Note    :
**************************************************************************************/

select id,job,score,r 
from (
	select *,
	rank()over(partition by job order by score desc)as r,
	count(*)over(partition by job)as t
	from grade
) as A
where round(abs(r-(t+1)/2)*1.0,2)<1
order by id
;