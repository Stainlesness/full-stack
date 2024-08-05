from datetime import date
from app import create_app, db
from app.models import Student, Fee, Payment

app = create_app()

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Create fees
    fees = [
        Fee(grade="1", term_fee=5000.0),
        Fee(grade="2", term_fee=5500.0),
        Fee(grade="3", term_fee=6000.0),
        Fee(grade="4", term_fee=6500.0),
    ]

    # Create students and initialize their balances
    students = [
        Student(name="Alice Smith", admission_number="5561", grade="1"),
        Student(name="Bob Jones", admission_number="5562", grade="2"),
        Student(name="Charlie Brown", admission_number="5563", grade="3"),
        Student(name="Daisy Johnson", admission_number="5564", grade="4"),
    ]
    for student in students:
        student.initialize_balance()

    # Create payments
    payments = [
        Payment(admission_number="5561", amount=5000.0, date=date(2024, 7, 1)),
        Payment(admission_number="5562", amount=5500.0, date=date(2024, 7, 1)),
        Payment(admission_number="5563", amount=6000.0, date=date(2024, 7, 1)),
        Payment(admission_number="5564", amount=6500.0, date=date(2024, 7, 1)),
    ]

    # Add all data to the session
    db.session.add_all(fees)
    db.session.add_all(students)
    db.session.add_all(payments)

    # Commit the changes
    db.session.commit()

    print("Database seeded successfully!")
