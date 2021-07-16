/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-16 16:37:27
# @File    : SQL81.sql
# @Note    :
**************************************************************************************/
select user_id, min(date) as first_date, next_date,count(*) as cnt
  from (select *,
               lead(date, 1) over(partition by user_id order by date asc) next_date
          from order_info
         where date > '2025-10-15'
           and status = 'completed'
           and product_name in ('C++', 'Python', 'Java'))
 group by user_id having count(*) >= 2
 order by 1