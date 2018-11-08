from app import db
 
 
class Staffing(db.Model):
    __tablename__ = "staffing"
 
    id = db.Column(db.Integer, primary_key=True)
    work_period = db.Column(db.String)
    employee_name = db.Column(db.String)
    client_name = db.Column(db.String)
    role = db.Column(db.String)
    time_spent = db.Column(db.Integer)