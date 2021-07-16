/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-05-10 08:39:01
# @File    : SQL91.sql
# @Note    :
**************************************************************************************/


select t.id, t.name, t.grade_sum
from(
	select b.id, b.name, a.grade_sum, rank() over(order by a.grade_sum desc) as rn
	from(
		select user_id, sum(case when type='add' then grade_num else grade_num*(-1) end) as grade_sum
		from grade_info
		group by user_id
	)a
	join user b on a.user_id=b.id
)t 
where t.rn=1
;