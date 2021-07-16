/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 20210207
# @File    : SQL66.sql
# @Note    :
**************************************************************************************/

select e.date, round(sum(case e.type when "no_completed" then 1 else 0 end)/count(*),3) as p
from email e
join user u1 on e.send_id = u1.id
join user u2 on e.receive_id = u2.id
where u1.is_blacklist = 0 and u2.is_blacklist = 0
group by e.date
order by date