/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-19 14:04:52
# @File    : SQL82.sql
# @Note    :
**************************************************************************************/
select a.id,a.is_group_buy,
(case when b.name is null then 'None' else b.name end) as client_name
from(
    select id,client_id,is_group_buy 
    from order_info
    where user_id in(
        select user_id
        from order_info
        where status ='completed'  and date>'2025-10-15'
            and product_name in ('C++','Java','Python')
        group by user_id
    having count(*)>=2
    )
    and status ='completed'
    and date>'2025-10-15'
    and product_name in ('C++','Java','Python')
) a left join client b on a.client_id =b.id
order by a.id;