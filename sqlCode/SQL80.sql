/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-15 08:48:36
# @File    : SQL80.sql
# @Note    :
**************************************************************************************/
Select user_id, min(date) first_buy_date, count(user_id) cnt
from order_info
where status ='completed' and date > '2025-10-15'
and product_name in ('C++','Java','Python')
group by user_id
having count(user_id)>=2
order by user_id