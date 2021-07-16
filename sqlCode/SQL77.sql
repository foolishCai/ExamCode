/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-13 08:56:30
# @File    : SQL77.sql
# @Note    :
**************************************************************************************/

select user_id
from order_info
where date>'2025-10-15' 
    and status='completed' 
    and product_name in ('C++', 'Java', 'Python')
group by user_id
having count(1)>=2
order by user_id