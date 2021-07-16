/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-14 11:49:17
# @File    : SQL78.sql
# @Note    :
**************************************************************************************/

select id,user_id,product_name,status,client_id,date 
from(
	select *,count(id) over(partition by user_id) n 
	from order_info
	where status='completed' and date > '2025-10-15'
	and product_name in ('C++','Java','Python')
)o
where o.n >1
order by id