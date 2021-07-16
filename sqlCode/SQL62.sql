/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 20210207
# @File    : SQL62.sql
# @Note    :
**************************************************************************************/

select number
from grade
group by number
having count(*) >= 3