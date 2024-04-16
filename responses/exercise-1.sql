-- write your SQL here
select locationid, month(datetime) as 'month', round(sum(JSON_EXTRACT(details, '$.items[*].amount')), 2) as 'refundAmount'
from orderItems 
JOIN (transactions CROSS JOIN JSON_TABLE(details, '$[*]' COLUMNS id INT, amount INT) AS multiple_trans) /*CROSS JOIN UNNEST(details -> 'items') AS item;*/
  ON orderItems.id = exploded_items.id
where transactions.type = "refund"
group by locationid, month(datetime)
order by locationId, month(datetime)

--in the interest of time, i was able to figure out the concept and i'm sure there's some weird syntax thing,
--but i wasn't able to get 1 part of it to compile for a final check, but I listed two possible ways to do it using mysql or postgress
--hope that helps
