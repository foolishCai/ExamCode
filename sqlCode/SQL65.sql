/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 20210207
# @File    : SQL65.sql
# @Note    :
**************************************************************************************/

select p.id,p.name,t.content
from person p
left join task t on p.id = t.person_id
order by p.id