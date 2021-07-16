/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-08 08:54:17
# @File    : SQL74.sql
# @Note    :
**************************************************************************************/

select job, 
       floor((count(job)+1)/2) as `start`,
       ceiling((count(job)+1)/2) as `end`
from grade
group by job
order by job