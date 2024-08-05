// src/App.js
import React, { useState } from 'react';
import StudentList from './components/StudentList';
import AddStudent from './components/AddStudent';
import StudentDetails from './components/StudentDetails';
import PaymentsPerDay from './components/PaymentsPerDay';
import TotalPaymentsPerMonth from './components/TotalPaymentsPerMonth';
import PaymentsOverview from './components/PaymentsOverview';



const App = () => {
    const [selectedStudent, setSelectedStudent] = useState(null);

    return (
        <div>
            <h1>School Management System</h1>
            <StudentList onSelectStudent={setSelectedStudent} />
            {selectedStudent && <StudentDetails student={selectedStudent} />}
            <AddStudent />
            <PaymentsPerDay />
            <TotalPaymentsPerMonth />
        </div>
    );
};

export default App;
