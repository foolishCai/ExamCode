/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-25 16:50:56
# @File    : SQL86.sql
# @Note    :
**************************************************************************************/



select t.job
      ,concat(t.d_year, '-', t.d_month) as first_year_mon
      ,t.num as first_year_cnt
      ,concat(t1.d_year, '-', t1.d_month) as second_year_mon
      ,t1.num as second_year_cnt
from(
	select job
	      ,substr(date, 1, 4) as d_year
	      ,substr(date, 6, 2) as d_month
	      ,sum(num) as num
	from resume_info
    where substr(date, 1, 4)='2025'
	group by job
	        ,substr(date, 1, 4)
	        ,substr(date, 6, 2)
)t 
left join(
	select job
	      ,substr(date, 1, 4) as d_year
	      ,substr(date, 6, 2) as d_month
	      ,sum(num) as num
	from resume_info
	group by job
	        ,substr(date, 1, 4)
	        ,substr(date, 6, 2)
)t1 on t.job=t1.job and t.d_year+1 = t1.d_year and t.d_month=t1.d_month
order by concat(t.d_year, '-', t.d_month) desc, job desc