/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-03-31 08:59:04
# @File    : SQL72.sql
# @Note    :
**************************************************************************************/

select job, round(avg(score*1.000), 3) as avg
from grade
group by job
order by avg desc
;