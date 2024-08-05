// src/components/AddStudent.js
import React, { useState } from 'react';
import axios from 'axios';

const AddStudent = () => {
    const [student, setStudent] = useState({
        name: '',
        admission_number: '',
        grade: '',
        balance: ''
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('https://back-end2-dl6sdah86-stanoos-projects.vercel.app/students', student);
            alert('Student added successfully');
            setStudent({
                name: '',
                admission_number: '',
                grade: '',
                balance: ''
            });
        } catch (error) {
            console.error('Error adding student', error);
            alert('Failed to add student');
        }
    };

    return (
        <div>
            <h2>Add New Student</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Name"
                    value={student.name}
                    onChange={(e) => setStudent({ ...student, name: e.target.value })}
                    required
                />
                <input
                    type="text"
                    placeholder="Admission Number"
                    value={student.admission_number}
                    onChange={(e) => setStudent({ ...student, admission_number: e.target.value })}
                    required
                />
                <input
                    type="text"
                    placeholder="Grade"
                    value={student.grade}
                    onChange={(e) => setStudent({ ...student, grade: e.target.value })}
                    required
                />
                <input
                    type="number"
                    placeholder="Current Balance"
                    value={student.balance}
                    onChange={(e) => setStudent({ ...student, balance: e.target.value })}
                    required
                />
                <button type="submit">Add Student</button>
            </form>
        </div>
    );
};

export default AddStudent;
