/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-03-23 08:52:54
# @File    : SQL67-2.sql
# @Note    :
**************************************************************************************/


select u.name as u_n, c.name as c_n, lo.date as d
from login as lo
join (
	select user_id, max(date) date
    from login group by user_id
)t1 on lo.date = t1.date and lo.user_id = t1.user_id
join user u on u.id = lo.user_id
join client c on c.id = lo.client_id
order by u_n asc;