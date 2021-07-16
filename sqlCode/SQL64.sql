/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 20210207
# @File    : SQL64.sql
# @Note    :
**************************************************************************************/


select a.id, a.number, count(distinct b.number) t_rank
from passing_number a,passing_number b
where a.number <= b.number
group by a.id, a.number
order by t_rank asc;