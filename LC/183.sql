SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
SELECT customerId FROM Orders
)



/*
This query:
Uses a subquery to get all customerIds that have ordered from the Orders table.
Filters the Customers table to only return rows where the id is NOT IN the list of customerIds from the subquery.
This returns customers that don't have a match in the Orders table, meaning they have never ordered. */