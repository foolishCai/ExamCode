/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-05-10 08:28:45
# @File    : SQL89.sql
# @Note    :
**************************************************************************************/

select b.name, a.grade_sum
from(
	select user_id, sum(grade_num) as grade_sum
	from grade_info
	group by user_id
	order by grade_sum desc
	limit 1 
)a
join user b on a.user_id=b.id
;