/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-03-24 08:51:46
# @File    : SQL68.sql
# @Note    :
**************************************************************************************/


select round(t.fz/t.fm, 3) as p
from(
select count(distinct a.user_id) as fm
      ,count(distinct case when DATE_ADD(a.fst_date,INTERVAL 1 DAY)=b.date then a.user_id else null end) as fz
from(select user_id, min(date) as fst_date from login group by user_id) a
left join login b on a.user_id=b.user_id  
)t
;