from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(50), nullable=False)
    representing = db.Column(db.String(100), nullable=True)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f'<Staff {self.name}>'
        

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admission_number = db.Column(db.String(50), unique=True, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    arrears = db.Column(db.Float, default=0.0)
    term_fee = db.Column(db.Float, nullable=False)
    use_bus = db.Column(db.Boolean, nullable=False)
    bus_balance = db.Column(db.Float, default=0.0)

    payments = db.relationship('Payment', backref='student', lazy=True)

    def set_password(self, password):
        self.admission_number = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.admission_number.encode('utf-8'))

    def initialize_balance(self):
        fee = Fee.query.filter_by(grade=self.grade).first()
        if fee:
            self.balance = fee.term_fee + self.arrears

class Fee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), unique=True, nullable=False)
    term_fee = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Fee {self.grade} - {self.term_fee}>'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(50), db.ForeignKey('student.admission_number'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    method = db.Column(db.String(15))

    @staticmethod
    def record_payment(admission_number, amount,method):
        student = Student.query.filter_by(admission_number=admission_number).first()
        if not student:
            raise ValueError("Student not found")
        student.balance -= amount
        student.arrears = 0  # Reset arrears on payment
        payment = Payment(admission_number=admission_number, amount=amount, method=method)
        db.session.add(payment)
        db.session.commit()
        return payment

class BusPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(50), db.ForeignKey('student.admission_number'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<BusPayment {self.admission_number} - {self.amount}>'

class BusDestinationCharges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    charge = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<BusDestination {self.destination} - {self.charge}>'

class BoardingFee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), nullable=False)
    extra_fee = db.Column(db.Float, nullable=False, default=3500)

    def __repr__(self):
        return f'<BoardingFee {self.grade} - {self.extra_fee}>'

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Assignment {self.title} for Grade {self.grade}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Event {self.title} on {self.date}>'

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Gallery Image {self.id}>'

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Notification {self.id} - {self.message}>'
        