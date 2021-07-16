/**************************************************************************************
# @author  : cai
# @email   : chenyw_work@yeah.net
# @time    : 2021-03-26 08:54:52
# @file    : SQL70.sql
# @note    :
**************************************************************************************/

-- 联立两表
-- 每个日期新用户的次日留存数/每个日期登录新用户的个数 即为每个日期新用户留存率
	select one.date, ifnull(round(two.counts/one.sum,3),0) p 
	from(
        #每个日期新用户的次日留存数
		select l.date,ifnull(t.sum,0) sum
		from login l
		left join(
			select date,count(user_id) sum
			from login l1
			where user_id not in(
				select user_id from login l2
				where l2.date < l1.date
			)
			group by date
		) t
		on l.date = t.date
		group by l.date
		order by l.date
	)as one
	join
	(
		#每个日期登录新用户的个数
        select distinct l.date,ifnull(t.sum,0) counts
		from login l
		left join(
			select date_sub(date,interval 1 day) date,count(user_id) sum
			from login
			where (user_id,date) in (
				select user_id,date_add(min(date),interval 1 day) date
				from login	
				group by user_id
			)
			group by date
		)t
		on l.date = t.date
		order by l.date
	)two
	on one.date = two.date
    order by one.date
 ;