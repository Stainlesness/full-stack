from datetime import datetime
from app import db  # Import db from the app module


# Staff can represent many classes
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Keep the password field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(50), nullable=False)
    # Represent many classes (one-to-many relationship)
    classes = db.relationship('Class', backref='staff', lazy=True)

    def __repr__(self):
        return f'<Staff {self.name}>'


# Each student can have many payments, bus payments, and assignments
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
    password = db.Column(db.String(100), nullable=False)  # Keep the password field

    # Relationships
    payments = db.relationship('Payment', backref='student', lazy=True)
    bus_payments = db.relationship('BusPayment', backref='student', lazy=True)
    assignments = db.relationship('Assignment', backref='student', lazy=True)

    def initialize_balance(self):
        fee = Fee.query.filter_by(grade=self.grade).first()
        if fee:
            self.balance = (fee.term_fee or 0) + (self.arrears or 0)
        else:
            # Handle the case where there is no fee record for the grade
            self.balance = self.arrears  # or set it to 0.0, or whatever is appropriate

    def __repr__(self):
        return f'<Student {self.name}, Grade {self.grade}>'


# Fee model where each grade can have only one fee (One-to-One for grade)
class Fee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), unique=True, nullable=False)  # One fee per grade
    term_fee = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Fee {self.grade} - {self.term_fee}>'


# Payment model where students can have many payments
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  # Foreign key to Student
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    method = db.Column(db.String(15))

    @staticmethod
    def record_payment(student_id, amount, method):
        student = Student.query.get(student_id)
        if not student:
            raise ValueError("Student not found")
        student.balance -= amount
        student.arrears = 0  # Reset arrears on payment
        payment = Payment(student_id=student_id, amount=amount, method=method)
        db.session.add(payment)
        db.session.commit()
        return payment


# Bus Payment model, many payments can be made by one student
class BusPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  # Foreign key to Student
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<BusPayment {self.student_id} - {self.amount}>'


# Charges per bus destination
class BusDestinationCharges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    charge = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<BusDestination {self.destination} - {self.charge}>'


# Boarding fees, linked to grades
class BoardingFee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), nullable=False)
    extra_fee = db.Column(db.Float, nullable=False, default=3500)

    def __repr__(self):
        return f'<BoardingFee {self.grade} - {self.extra_fee}>'


# Assignments can be related to multiple students
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  # Foreign key to Student

    def __repr__(self):
        return f'<Assignment {self.title} for Grade {self.grade}>'


# Class model to represent the classes that staff can manage
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)  # One-to-Many relationship to Staff

    def __repr__(self):
        return f'<Class {self.name}>'


# School Events
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Event {self.title} on {self.date}>'


# School Gallery for Images
class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Gallery Image {self.id}>'


# Notifications
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Notification {self.id} - {self.message}>'
    
