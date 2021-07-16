/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-21 09:26:00
# @File    : SQL83.sql
# @Note    :
**************************************************************************************/

select (case is_group_buy when 'Yes' then 'GroupBuy' else c.name end) source
      ,count(*)
from order_info o 
left join client c on o.client_id=c.id
where user_id in(
	select user_id
	from order_info
	where date > '2025-10-15'
		and product_name in ('Python','Java','C++')
		and status = 'completed'
	group by user_id having count(*)>=2
)
	and date > '2025-10-15'
	and product_name in ('Python','Java','C++')
	and status = 'completed'
group by source
order by source