from datetime import datetime
from app import db  # Import db from the app module

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admission_number = db.Column(db.String(50), unique=True, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def initialize_balance(self):
        fee = Fee.query.filter_by(grade=self.grade).first()
        if fee:
            self.balance = fee.term_fee

class Fee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), unique=True, nullable=False)
    term_fee = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    @staticmethod
    def record_payment(admission_number, amount, date):
        student = Student.query.filter_by(admission_number=admission_number).first()
        if not student:
            raise ValueError("Student not found")
        student.balance -= amount
        payment = Payment(admission_number=admission_number, amount=amount, date=date)
        db.session.add(payment)
        db.session.commit()
        return payment
