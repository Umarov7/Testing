"""+----+------------+-----------+---------------+------------+--------+
| id | first_name | last_name | phone_number  | job_id     | salary |
+----+------------+-----------+---------------+------------+--------+
|  1 | Steven     | King      | +998941234567 | AD_PRES    |  24000 |
|  2 | Neena      | Kochnar   | +998941244668 | AD_VP      |  17000 |
|  3 | Lex        | De Haan   | +998941244669 | AD_VP      |  17000 |
|  4 | Aleksandr  | Hunold    | +998941244670 | IT_PROG    |  11000 |
|  5 | Bruce      | Ernest    | +998941244671 | IT_PROG    |   8000 |
|  6 | David      | Austin    | +998941244871 | IT_PROG    |   6800 |
|  7 | Valli      | Pataballa | +998941244975 | IT_PROG    |   6800 |
|  8 | Diana      | Lorentz   | +998946254976 | IT_PROG    |   6200 |
|  9 | Nancy      | Greenberg | +998946255946 | FI_MGR     |  12000 |
| 10 | Daniel     | Faviet    | +998946755948 | FI_ACCOUNT |   9000 |
| 11 | John       | Chen      | +998946756953 | FI_ACCOUNT |   8200 |
| 12 | Ismeal     | Sciarra   | +998946856983 | FI_ACCOUNT |   7700 |
| 13 | Den        | Raphaely  | +998946886983 | PU_MAN     |  11000 |
| 14 | Aleksandr  | Kahoo     | +998946884983 | PU_CLERK   |   3100 |
+----+------------+-----------+---------------+------------+--------+"""

'use Employee_db-database'
# 1-task
'Select first_name,last_name from Staff-table;'
# 2-task
'Select  first_name,last_name,salary from Staff-table where job_id = IT_PROG;'
# 3-task
'Select job_id,salary from Staff-table where salary > 5000 and salary < 20000;'
# 4-task
'Select salary from Staff-table where job_id IN ("IT_PROG","FI_ACCOUNT");'
# 5-task
'Select * from Staff-table where phone_number like "%6983";'
# 6-task
'Sum(salary) from Staff-table'
# 7-task
'Select * from Staff-table where job_id = IT_PROG and salary = (SELECT MAX(salary) FROM Staff_table WHERE job_id = "IT_PROG");'
# 8-task
'Select * from Staff-table where salary > (Select AVG(salary) from Staff-table);'
# 9-task
'Select * from Staff-table where salary > (Select Sum(salary) / Count(*) from Staff-table where job_id = "IT_PROG");'