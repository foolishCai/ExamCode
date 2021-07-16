/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-26 09:25:51
# @File    : SQL87.sql
# @Note    :
**************************************************************************************/

SELECT grade,sum(number)over(order by grade) as t_rank
from class_grade 