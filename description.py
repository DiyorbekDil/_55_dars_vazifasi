"""
Tables:

companies ->
id SERIAL PRIMARY KEY
name VARCHAR(64) NOT NULL
est_year SMALLINT NOT NULL

departments ->
id SERIAL PRIMARY KEY
name VARCHAR(64) NOT NULL
company_id INTEGER
FOREIGN KEY (company_id) REFERENCES companies(id)

employees ->
id SERIAL PRIMARY KEY
first_name VARCHAR(64) NOT NULL
last_name VARCHAR(64) NOT NULL
age INTEGER NOT NULL
email VARCHAR(64) NOT NULL
gender VARCHAR(5) NOT NULL
experience SMALLINT NOT NULL
department_id INTEGER
FOREIGN KEY (department_id) REFERENCES departments(id)


Statistical data:

1. Number of companies

2. Number of departments of each company

3. Number of employees of each company
4. Number of male workers of each company
5. Number of female workers of each company
6. Number of all workers

7. Number of workers with more than 2 years of experience
8. Number of male workers with more than 2 years of experience
9. Number of female workers with more than 2 years of experience

10. Number of workers with more than 2 years of experience of each company
11. Number of male workers with more than 2 years of experience of each company
12. Number of female workers with more than 2 years of experience of each company

13. Average age of all workers
14. Average age of workers of each company

15. Average experience of all workers
16. Average experience of workers of each company

17. Number of companies established after 2000
18. Average established year of all companies

"""