-- group by scores and sort
SELECT score, COUNT(*) as number FROM second_table
GROUP BY score
ORDER BY number DESC;
