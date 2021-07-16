/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-06 10:53:32
# @File    : SQL73.sql
# @Note    :
**************************************************************************************/

select a.* 
from grade a
join (select job,avg(score) as score from grade group by job) b on a.job=b.job and a.score>b.score
order by a.id