from db_manager import execute_query


def create_tables():
    commands = [
        """
        create table if not exists companies (
                id serial primary key, 
                name varchar(64) not null, 
                est_year smallint not null
        );
        """,
        """
        create table if not exists departments (
                id serial primary key,
                name varchar(64) not null,
                company_id integer,
                foreign key (company_id) references companies(id)
        );
        """,
        """
        create table if not exists employees (
                id serial primary key,
                first_name varchar(64) not null,
                last_name varchar(64) not null,
                age integer not null,
                email varchar(64) not null,
                gender varchar(5) not null,
                experience smallint not null,
                department_id integer,
                foreign key (department_id) references departments(id)
        );
        """
    ]

    for command in commands:
        execute_query(command)


if __name__ == '__main__':
    print(create_tables())

