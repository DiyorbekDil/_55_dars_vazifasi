from statistical_functions import num_of_companies, num_of_dept_each_comp
from statistical_functions import num_of_emp_of_each_comp, num_of_male_emp_of_each_comp
from statistical_functions import num_of_female_emp_of_each_comp, num_of_all_workers
from statistical_functions import num_of_workers_2_years_exp, num_of_male_workers_2_years_exp
from statistical_functions import num_of_female_workers_2_years_exp, num_of_workers_2_years_of_each_comp
from statistical_functions import num_of_male_workers_2_years_of_each_comp
from statistical_functions import num_of_female_workers_2_years_of_each_comp
from statistical_functions import avg_age_of_all_workers, avg_age_of_all_workers_of_each_comp
from statistical_functions import avg_exp_of_all_workers, avg_exp_of_all_workers_of_each_comp
from statistical_functions import avg_est_year, num_of_comp_est_after_2000


def menu():
    text = """
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
    19. Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        num_of_companies()
    elif user_input == '2':
        num_of_dept_each_comp()
    elif user_input == '3':
        num_of_emp_of_each_comp()
    elif user_input == '4':
        num_of_male_emp_of_each_comp()
    elif user_input == '5':
        num_of_female_emp_of_each_comp()
    elif user_input == '6':
        num_of_all_workers()
    elif user_input == '7':
        num_of_workers_2_years_exp()
    elif user_input == '8':
        num_of_male_workers_2_years_exp()
    elif user_input == '9':
        num_of_female_workers_2_years_exp()
    elif user_input == '10':
        num_of_workers_2_years_of_each_comp()
    elif user_input == '11':
        num_of_male_workers_2_years_of_each_comp()
    elif user_input == '12':
        num_of_female_workers_2_years_of_each_comp()
    elif user_input == '13':
        avg_age_of_all_workers()
    elif user_input == '14':
        avg_age_of_all_workers_of_each_comp()
    elif user_input == '15':
        avg_exp_of_all_workers()
    elif user_input == '16':
        avg_exp_of_all_workers_of_each_comp()
    elif user_input == '17':
        num_of_comp_est_after_2000()
    elif user_input == '18':
        avg_est_year()
    elif user_input == '19':
        return
    else:
        print('Unexpected number!')
        return menu()
    return menu()


if __name__ == '__main__':
    menu()
