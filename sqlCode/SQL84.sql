/**************************************************************************************
# @Author  : Cai
# @Email   : chenyw_work@yeah.net
# @Time    : 2021-04-22 09:14:16
# @File    : SQL84.sql
# @Note    :
**************************************************************************************/
SELECT job,SUM(num) AS cnt
FROM resume_info
WHERE year(date) = 2025
GROUP by job
ORDER BY cnt DESC;