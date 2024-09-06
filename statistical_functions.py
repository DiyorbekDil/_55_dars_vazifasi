from db_manager import execute_query


def num_of_companies():
    command = """SELECT COUNT(*) FROM companies;"""
    print("Number of companies: ", execute_query(command, fetch='one')[0])


def num_of_dept_each_comp():
    command = """SELECT c.name, COUNT(d.name) 
            FROM 
                companies c 
            INNER JOIN
                departments d on c.id = d.company_id 
            GROUP BY
                c.name
    """
    results = execute_query(command, fetch='all')
    print('Company - number of departments')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_emp_of_each_comp():
    command = """
        SELECT 
        c.name AS company_name,
        COUNT(e.id) AS employee_count
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - number of employees')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_male_emp_of_each_comp():
    command = """
        SELECT 
        c.name AS company_name,
        COUNT(e.id) AS employee_count
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    WHERE
        e.gender = 'man'
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - number of male workers')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_female_emp_of_each_comp():
    command = """
        SELECT 
        c.name AS company_name,
        COUNT(e.id) AS employee_count
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    WHERE 
        e.gender = 'woman'
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - number of female workers')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_all_workers():
    command = """SELECT COUNT(*) FROM employees;"""
    print("Number of all workers: ", execute_query(command, fetch='one')[0])


def num_of_workers_2_years_exp():
    print("Number of workers with more than 2 years of experience: ", end='')
    command = """SELECT COUNT(*) FROM employees WHERE experience > 2;"""
    print(execute_query(command, fetch='one')[0])


def num_of_male_workers_2_years_exp():
    print("Number of male workers with more than 2 years of experience: ", end='')
    command = """SELECT COUNT(*) FROM employees WHERE experience > 2 and gender='man';"""
    print(execute_query(command, fetch='one')[0])


def num_of_female_workers_2_years_exp():
    print("Number of female workers with more than 2 years of experience: ", end='')
    command = """SELECT COUNT(*) FROM employees WHERE experience > 2 and gender='woman';"""
    print(execute_query(command, fetch='one')[0])


def num_of_workers_2_years_of_each_comp():
    command = """
    SELECT 
        c.name AS company_name,
        COUNT(e.id) AS employee_count
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    WHERE
        e.experience > 2
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - number of workers with more than 2 years experience')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_male_workers_2_years_of_each_comp():
    command = """
    SELECT 
        c.name AS company_name,
        COUNT(e.id) AS employee_count
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    WHERE
        e.experience > 2 and e.gender='man'
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - number of male workers with more than 2 years experience')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_female_workers_2_years_of_each_comp():
    command = """
    SELECT 
        c.name AS company_name,
        COUNT(e.id) AS employee_count
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    WHERE
        e.experience > 2 and e.gender='woman'
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - number of female workers with more than 2 years experience')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def avg_age_of_all_workers():
    command = """SELECT AVG(age) as avg_age FROM employees;"""
    print("Average age of all workers: ", execute_query(command, fetch='one')[0])


def avg_age_of_all_workers_of_each_comp():
    command = """
    SELECT 
        c.name AS company_name,
        AVG(e.age) AS avg_worker_age
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - average age of workers')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def avg_exp_of_all_workers():
    command = """SELECT AVG(experience) as avg_exp FROM employees;"""
    print("Average experience of all workers: ", execute_query(command, fetch='one')[0])


def avg_exp_of_all_workers_of_each_comp():
    command = """
    SELECT 
        c.name AS company_name,
        AVG(e.experience) AS avg_worker_experience
    FROM 
        companies c
    INNER JOIN 
        departments d ON c.id = d.company_id
    INNER JOIN 
        employees e ON d.id = e.department_id
    GROUP BY 
        c.id, c.name;
    """
    results = execute_query(command, fetch='all')
    print('Company - average experience of workers')
    for result in results:
        print(f"{result[0]} - {result[1]}")


def num_of_comp_est_after_2000():
    command = """SELECT COUNT(*) FROM companies WHERE est_year > 2000;"""
    print("Number of companies established after 2000: ",
                execute_query(command, fetch='one')[0])


def avg_est_year():
    command = """SELECT AVG(est_year) FROM companies;"""
    print("Average established year of all companies: ",
          execute_query(command, fetch='one')[0])

