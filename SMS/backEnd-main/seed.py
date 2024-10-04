from datetime import datetime, date
from app import create_app, db
from app.models import Student, Fee, Payment, Staff, Assignment, Event, Gallery, Notification
import bcrypt

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
        Fee(grade="5", term_fee=7000.0),
    ]

    # Create students and initialize their balances
    students = [
        Student(name="Alice Smith", admission_number="5561", grade="1", term_fee=5000.0, use_bus=False),
        Student(name="Bob Jones", admission_number="5562", grade="2", term_fee=5500.0, use_bus=True),
        Student(name="Charlie Brown", admission_number="5563", grade="3", term_fee=6000.0, use_bus=True),
        Student(name="Daisy Johnson", admission_number="5564", grade="4", term_fee=6500.0, use_bus=False),
        Student(name="Ethan Hunt", admission_number="5565", grade="5", term_fee=7000.0, use_bus=True),
    ]
    for student in students:
        student.initialize_balance()

    # Create staff
    staff_members = [
        Staff(name="John Doe", phone="0712345678", role="Teacher", representing="Class 1"),
        Staff(name="Jane Smith", phone="0723456789", role="Bursar", representing="Finance Department"),
        Staff(name="Mark Taylor", phone="0734567890", role="Director", representing="Administration"),
        Staff(name="Lucy Brown", phone="0745678901", role="Admin", representing="School Office"),
        Staff(name="Tom White", phone="0756789012", role="Teacher", representing="Class 2"),
    ]
    
    # Set passwords for staff members
    for staff in staff_members:
        staff.set_password("password123")  # Replace with a stronger password if needed

    # Create assignments
    assignments = [
        Assignment(title="Math Homework", grade="1", description="Complete exercises from chapter 1.", due_date=datetime(2024, 10, 15)),
        Assignment(title="Science Project", grade="2", description="Prepare a presentation on the solar system.", due_date=datetime(2024, 10, 22)),
        Assignment(title="History Essay", grade="3", description="Write an essay about the history of your country.", due_date=datetime(2024, 10, 29)),
        Assignment(title="English Reading", grade="4", description="Read the assigned chapters and summarize.", due_date=datetime(2024, 11, 5)),
        Assignment(title="Art Class", grade="5", description="Create a drawing of your favorite place.", due_date=datetime(2024, 11, 12)),
    ]

    # Create events
    events = [
        Event(title="Sports Day", date=datetime(2024, 11, 20), destination="School Ground", description="Annual sports event."),
        Event(title="Parent-Teacher Meeting", date=datetime(2024, 11, 27), destination="Main Hall", description="Discussion about student progress."),
        Event(title="Field Trip to Museum", date=datetime(2024, 12, 5), destination="Local Museum", description="Educational trip for students."),
        Event(title="Christmas Celebration", date=datetime(2024, 12, 20), destination="School Hall", description="Celebration of Christmas."),
        Event(title="Graduation Ceremony", date=datetime(2025, 1, 15), destination="Auditorium", description="Graduation for year-end students."),
    ]

    # Create gallery images
    galleries = [
        Gallery(image_url="http://example.com/image1.jpg", description="School Opening Day"),
        Gallery(image_url="http://example.com/image2.jpg", description="Science Fair 2024"),
        Gallery(image_url="http://example.com/image3.jpg", description="Art Exhibition"),
        Gallery(image_url="http://example.com/image4.jpg", description="Sports Day 2024"),
        Gallery(image_url="http://example.com/image5.jpg", description="Graduation Ceremony 2024"),
    ]

    # Create notifications
    notifications = [
        Notification(message="School will be closed on December 12th for a public holiday."),
        Notification(message="Please ensure all fees are paid by December 1st."),
        Notification(message="The science fair will take place on January 10th."),
        Notification(message="Reminder: Parent-teacher meetings next week."),
        Notification(message="Winter break starts on December 20th."),
    ]

    # Create payments
    payments = [
        Payment(admission_number="5561", amount=5000.0, date=date(2024, 7, 1), method="cash"),
        Payment(admission_number="5562", amount=5500.0, date=date(2024, 7, 1), method="inkind"),
        Payment(admission_number="5563", amount=6000.0, date=date(2024, 7, 1), method="paybill"),
        Payment(admission_number="5564", amount=6500.0, date=date(2024, 7, 1), method="cash"),
        Payment(admission_number="5565", amount=7000.0, date=date(2024, 7, 1), method="inkind"),
    ]

    # Add all data to the session
    db.session.add_all(fees)
    db.session.add_all(students)
    db.session.add_all(staff_members)
    db.session.add_all(assignments)
    db.session.add_all(events)
    db.session.add_all(galleries)
    db.session.add_all(notifications)
    db.session.add_all(payments)

    # Commit the changes
    db.session.commit()

    print("Database seeded successfully!")
    