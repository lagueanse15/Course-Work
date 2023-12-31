SELECT *
FROM survey
LIMIT 10;

SELECT question,
   COUNT(DISTINCT user_id) AS 'responses',  1.0 * COUNT(DISTINCT user_id) 
/ 500 AS 'PropOfResps2Q'
FROM survey
GROUP BY question;

SELECT DISTINCT q.user_id AS 'user_id',
   h.user_id IS NOT NULL AS 'try_on_at_home',
   h.number_of_pairs,
   p.user_id IS NOT NULL AS 'is_purchase'
FROM quiz AS q
LEFT JOIN home_try_on AS h
   ON q.user_id = h.user_id
LEFT JOIN purchase AS p
   ON p.user_id = q.user_id
LIMIT 10;
