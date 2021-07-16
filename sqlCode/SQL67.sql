/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 20210207
# @File    : SQL67.sql
# @Note    :
**************************************************************************************/


select user_id, max(date) as d
from login
group by user_id
order by user_id
;