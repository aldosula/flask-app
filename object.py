from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Student(db.Model):
    __tablename__ = "students"
 
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer(),unique = True)
    studentFullName = db.Column(db.String())
    studentAge = db.Column(db.Integer())
    

    def __init__(self, studentId,studentFullName,studentAge):
        self.studentId = studentId
        self.studentFullName = studentFullName
        self.studentAge = studentAge
        
 
   