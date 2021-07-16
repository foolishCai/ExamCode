/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-23 10:17:45
# @File    : SQL85.sql
# @Note    :
**************************************************************************************/

SELECT
    job,
    DATE_FORMAT(date,'%Y-%m') as mon
    ,sum(num) as cnt
FROM resume_info ri
where DATE_FORMAT(date,'%Y')  = '2025'
group by job,mon
order by mon desc,cnt desc