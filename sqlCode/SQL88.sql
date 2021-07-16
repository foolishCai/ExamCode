/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-27 17:39:50
# @File    : SQL88.sql
# @Note    :
**************************************************************************************/
select grade from (
    select grade
    ,(select sum(number) from class_grade) as 'total'
    ,sum(number) over(order by grade) a
    ,sum(number) over(order by grade desc) b
     from class_grade) t1
where a >= total/2 and b >=total/2
order by grade
;