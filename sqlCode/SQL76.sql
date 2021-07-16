/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-12 08:58:31
# @File    : SQL76.sql
# @Note    :
**************************************************************************************/

select id,user_id,product_name,status,client_id, date
from order_info
where status = 'completed'
	and product_name in ("Java","C++","Python")
	and date > "2025-10-15"
order by id