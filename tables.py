from flask_table import Table, Col
 
class Results(Table):
    id = Col('Id', show=False)
    employee_name = Col('Employee')
    client_name = Col('Client')
    role = Col('Role')
    time_spent = Col('Time Spent')