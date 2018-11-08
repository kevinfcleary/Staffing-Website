# main.py
 
from app import app
from db_setup import init_db, db_session
from forms import StaffSearchForm, StaffForm
from flask import flash, render_template, request, redirect
from models import Staffing
from tables import Results
 
init_db()
 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    search = StaffSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search)
 
 
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search_string:
        if search.data['select'] == 'Client':
            qry = db_session.query(Staffing).filter(
                    Staffing.client_name.contains(search_string))
            results = qry.order_by(Staffing.role).all()
        elif search.data['select'] == 'Employee':
            qry = db_session.query(Staffing).filter(
                Staffing.employee_name.contains(search_string))
            results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)
		
@app.route('/new_record', methods=['GET', 'POST'])
def new_record():
    """
    Add a new record
    """
    form = StaffForm(request.form)
 
    if request.method == 'POST' and form.validate():
        # save the album
        staff = Staffing()
        save_changes(staff, form, new=True)
        flash('Record created successfully!')
        return redirect('/')
 
    return render_template('new_record.html', form=form)
	
def save_changes(record, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    record = Staffing()
    record.employee_name = form.employee_name.data
    record.client_name = form.client_name.data
    record.role = form.role.data
    record.time_spent = form.time_spent.data
 
    if new:
        # Add the new album to the database
        db_session.add(record)
 
    # commit the data to the database
    db_session.commit()
 
if __name__ == '__main__':
    app.run()