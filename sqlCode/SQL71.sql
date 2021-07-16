/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-03-29 09:09:22
# @File    : SQL71.sql
# @Note    :
**************************************************************************************/
SELECT name AS u_n, date
      ,sum(number) over(partition by user_id order by date) AS ps_num
FROM passing_number,user
WHERE passing_number.user_id=user.id
GROUP BY date,u_n
ORDER BY date,u_n