// src/components/StudentList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentList = ({ onSelectStudent }) => {
    const [students, setStudents] = useState([]);
    const [gradeFilter, setGradeFilter] = useState('');

    useEffect(() => {
        fetchStudents();
    }, [gradeFilter]);

    const fetchStudents = async () => {
        try {
            const response = await axios.get('https://back-end2-dl6sdah86-stanoos-projects.vercel.app/students', {
                params: { grade: gradeFilter }
            });
            setStudents(response.data);
        } catch (error) {
            console.error('Error fetching students', error);
        }
    };

    return (
        <div>
            <h2>Students</h2>
            <input
                type="text"
                placeholder="Filter by grade"
                value={gradeFilter}
                onChange={(e) => setGradeFilter(e.target.value)}
            />
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Admission Number</th>
                        <th>Balance</th>
                        <th>Grade</th>
                    </tr>
                </thead>
                <tbody>
                    {students.map((student) => (
                        <tr key={student.id} onClick={() => onSelectStudent(student)}>
                            <td>{student.name}</td>
                            <td>{student.admission_number}</td>
                            <td>{student.balance}</td>
                            <td>{student.grade}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default StudentList;
