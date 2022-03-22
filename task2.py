from flask import Flask, request, render_template, redirect
from object import db,Student
import logging
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()


@app.route("/students")
def showStudents():
    students = Student.query.all()
    return render_template('showStudents.html',students = students)


@app.route("/students/create", methods = ['GET','POST'])
def createStudents():
    if request.method == 'GET':
        return render_template('createStudent.html')

    if request.method == 'POST':
        studentId = request.form['studentId']
        studentFullName = request.form['studentFullName']
        studentAge = request.form['studentAge']
        student = Student(studentId=studentId, studentFullName=studentFullName, studentAge=studentAge)
       
       
        db.session.add(student)
        db.session.commit()
        return redirect('/students')

@app.route('/students/update/<int:id>',methods = ['GET','POST'])
def updateStudent(id):
    student = Student.query.filter_by(studentId=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            studentFullName = request.form['studentFullName']
            studentAge = request.form['studentAge']
            student = Student(studentId=id, studentFullName=studentFullName, studentAge= studentAge)
            db.session.add(student)
            db.session.commit()
            return redirect(f'/students/{id}')
        return f"Student Not Found"
 
    return render_template('updateStudent.html', student = student)


@app.route('/students/delete/<int:id>', methods=['GET','POST'])
def deleteStudent(id):
    student = Student.query.filter_by(studentId=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect('/students')
        return f"Student not found"
 
    return render_template('deleteStudent.html',  student = student)


@app.route('/students/<int:id>')
def getStudents(id):
    student = Student.query.filter_by(studentId=id).first()
    if student:
        return render_template('studentInfo.html', student = student)
    return f"Student not found"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)