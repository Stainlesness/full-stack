from datetime import datetime
from app import create_app, db
from app.models import (
    Student, Fee, Payment, Staff, Assignment, Event, Gallery, Notification, 
    BoardingFee, BusDestinationCharges, BusPayment
)

app = create_app()


with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Step 1: Seed Fees
    fees = [
        Fee(grade="1", term_fee=5000.0),
        Fee(grade="2", term_fee=5500.0),
        Fee(grade="3", term_fee=6000.0),
        Fee(grade="4", term_fee=6500.0),
        Fee(grade="5", term_fee=7000.0),
        Fee(grade="6", term_fee=7500.0),
        Fee(grade="7", term_fee=8000.0),
        Fee(grade="8", term_fee=8500.0),
    ]
    db.session.add_all(fees)
    db.session.commit()  # Commit fees to ensure they exist for initializing student balances

    # Step 2: Seed Boarding Fees
    boarding_fees = [
        BoardingFee(grade="6", extra_fee=3500.0),
        BoardingFee(grade="7", extra_fee=3500.0),
        BoardingFee(grade="8", extra_fee=3500.0),
    ]
    db.session.add_all(boarding_fees)
    db.session.commit()

    # Step 3: Seed Bus Destination Charges
    bus_destination_charges = [
        BusDestinationCharges(destination="Downtown", charge=1500.0),
        BusDestinationCharges(destination="Uptown", charge=2000.0),
    ]
    db.session.add_all(bus_destination_charges)
    db.session.commit()

    # Step 4: Seed Students
    students = [
        Student(name="Alice Smith", admission_number="5561", grade="1", use_bus=False, term_fee=5000.0),
        Student(name="Bob Jones", admission_number="5562", grade="2", use_bus=True, term_fee=5500.0),
        Student(name="Charlie Brown", admission_number="5563", grade="3", use_bus=False, term_fee=6000.0),
        Student(name="Daisy Johnson", admission_number="5564", grade="4", use_bus=True, term_fee=6500.0),
        Student(name="Eve Adams", admission_number="5565", grade="5", use_bus=False, term_fee=7000.0),
        Student(name="Frank Miller", admission_number="5566", grade="6", use_bus=True, term_fee=7500.0),
        Student(name="Grace Lee", admission_number="5567", grade="7", use_bus=False, term_fee=8000.0),
        Student(name="Henry Davis", admission_number="5568", grade="8", use_bus=True, term_fee=8500.0),
    ]

    for student in students:
        student.initialize_balance()

    db.session.add_all(students)
    db.session.commit()

    # Step 5: Seed Staff
    staff_members = [
        Staff(name="Principal Smith", phone="0712345678", role="Principal", representing="All grades"),
        Staff(name="Bursar Jane", phone="0712345679", role="Bursar", representing="Finance"),
        Staff(name="Teacher Tom", phone="0712345680", role="Teacher", representing="Grade 1"),
    ]

    for staff in staff_members:
        staff.set_password("password123")

    db.session.add_all(staff_members)
    db.session.commit()

    # Step 6: Seed Payments
    payments = [
        Payment(admission_number="5561", amount=2500.0, method="Cash"),
        Payment(admission_number="5562", amount=2000.0, method="Mpesa"),
    ]
    db.session.add_all(payments)
    db.session.commit()

    # Step 7: Seed Bus Payments
    bus_payments = [
        BusPayment(admission_number="5562", amount=1500.0),  # For "Downtown" destination
        BusPayment(admission_number="5564", amount=2000.0),  # For "Uptown" destination
    ]
    db.session.add_all(bus_payments)
    db.session.commit()

    # Step 8: Seed Assignments
    assignments = [
        Assignment(title="Math Homework", grade="1", description="Complete exercises 1 to 10", due_date=datetime(2024, 10, 10)),
        Assignment(title="Science Project", grade="2", description="Create a model of the solar system", due_date=datetime(2024, 10, 15)),
    ]
    db.session.add_all(assignments)
    db.session.commit()

    # Step 9: Seed Events
    events = [
        Event(title="School Sports Day", date=datetime(2024, 10, 20), destination="School Grounds", description="Annual sports competition for all grades"),
        Event(title="Parent-Teacher Meeting", date=datetime(2024, 10, 25), destination="School Hall", description="Discuss student progress with parents"),
    ]
    db.session.add_all(events)
    db.session.commit()

    # Step 10: Seed Gallery
    galleries = [
        Gallery(image_url="http://example.com/image1.jpg", description="Sports Day 2023"),
        Gallery(image_url="http://example.com/image2.jpg", description="School Trip to the Museum"),
    ]
    db.session.add_all(galleries)
    db.session.commit()

    # Step 11: Seed Notifications
    notifications = [
        Notification(message="School will be closed on 2024-10-15 for a public holiday."),
        Notification(message="Reminder: Parent-Teacher meeting on 2024-10-25."),
    ]
    db.session.add_all(notifications)
    db.session.commit()

    print("Database seeding completed successfully!")
