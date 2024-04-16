-- write your SQL here
select locationid, month(datetime) as 'month', round(sum(JSON_EXTRACT(details, '$.items[*].amount')), 2) as 'refundAmount'
from orderItems 
JOIN (transactions CROSS JOIN JSON_TABLE(details, '$[*]' COLUMNS id INT, amount INT) AS multiple_trans) /*CROSS JOIN UNNEST(details -> 'items') AS item;*/
  ON orderItems.id = exploded_items.id
where transactions.type = "refund"
group by locationid, month(datetime)
order by locationId, month(datetime)
