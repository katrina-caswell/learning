##### How to show a column from a table
```
SELECT field FROM table;
```

##### Showing multiple columns
```
SELECT field1, field2 FROM table;
```

##### Show all columns from a table
```
SELECT * FROM table;
```

##### Limit rows returned when showing a table, to make it run faster (e.g. to 10)
```
SELECT * FROM table LIMIT 10;
```

##### If rows contain duplicate values, use distinct to see only one of each value
```
SELECT DISTINCT country FROM table;
```

##### Find name and year for films released in the 90s that are French or Spanish and grossed more than 2M
```
SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish')
AND gross >2000000;
```

##### Find name and year of French or Spanish films that released between 1990 and 2000 inclusive and budgeted over 1M
```
SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND (language = 'Spanish' OR language = 'French');
```

##### Count rows
```
SELECT COUNT(*)
FROM films
WHERE language IS NULL;
```

```
SELECT event_type, COUNT(1) AS no_of_rows FROM database WHERE current='Y'
GROUP BY event_type
ORDER BY count(1) desc;
```

##### Use IN to save on having multiple OR statements
```
SELECT title, certification
FROM films
WHERE certification IN ('PG','R');
```

##### Like and not like - names beginning with B, names with R as the second letter, names that don't start with A
```
SELECT name
FROM people
WHERE name LIKE 'B%';
```

```
SELECT name
FROM people
WHERE name LIKE '_r%';
```

```
SELECT name
FROM people
WHERE name NOT LIKE 'A%';
```

##### Inner joins
```
SELECT *
FROM appointment a
INNER JOIN store s
ON a.database_storenum = s.storenumber
AND s.current='Y'
WHERE a.customerID = 123
AND s.storenumber = 1
ORDER BY bookingdate
```

Good table design would include singular field names - table = customer, fields = id, first_name, phone_num (not table = Customer, fields = IDS, FIRST NAMES, PHONE NUMS)

Aliasing - if there is a stupid field name, you can change it to something more readable so:
```
SELECT name AS first_name
FROM employees
```
Views - virtual tables
```
CREATE VIEW employee_hire_years AS
SELECT id, name, year_hired
FROM employees;
```
