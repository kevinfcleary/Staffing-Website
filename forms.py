# forms.py
 
from wtforms import Form, StringField, SelectField
 
class StaffSearchForm(Form):
    choices = [('Employee', 'Employee'),
               ('Client', 'Client')]
    select = SelectField('Search for staffing information:', choices=choices)
    search = StringField('')

class StaffForm(Form):
    time_choices = [('25', '25'),
                   ('50', '50'),
                   ('75', '75'),
				   ('100','100')
                   ]
	#role_choices = [('Lead','Lead'),
	#							('Quarterback', 'Quarterback'),
	#							('Team Member', 'Team Member')
	#							]
    employee_name = StringField('Employee')
    client_name = StringField('Client')
    role = StringField('Role')
    time_spent = SelectField('Time Spent', choices=time_choices)