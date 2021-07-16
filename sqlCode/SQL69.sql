/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-03-25 08:45:17
# @File    : SQL69.sql
# @Note    :
**************************************************************************************/


select t0.date
      ,sum(case when t.fst_date is not null then 1 else 0 end) as new
from(select date from login group by date) t0
left join(
	select user_id, min(date) as fst_date 
	from login group by user_id
)t on t0.date = t.fst_date
group by t0.date
order by t0.date
;