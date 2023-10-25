Задание 1

SELECT с.login, COUNT(*) AS total_orders_in_delivery
FROM "Couriers" AS с
LEFT JOIN "Orders" AS о ON с."courierId" = о."courierId"
WHERE о."inDelivery" = true
GROUP BY с.login;

Задание 2

SELECT
  track,
  CASE
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN inDelivery = true THEN 1
    ELSE 0
  END AS status
FROM "Orders";