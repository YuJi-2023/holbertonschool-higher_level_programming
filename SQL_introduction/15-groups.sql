-- group records by scores and display numbers of groups in new column

SELECT score, COUNT(*) AS number FROM second_table
	GROUP BY score 
	ORDER BY number DESC;

