// src/components/PaymentsPerDay.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PaymentsPerDay = () => {
    const [payments, setPayments] = useState([]);
    const [date, setDate] = useState('');

    useEffect(() => {
        if (date) {
            fetchPayments();
        }
    }, [date]);

    const fetchPayments = async () => {
        try {
            const response = await axios.get(`https://back-end2-dl6sdah86-stanoos-projects.vercel.app/payments`, {
                params: { date }
            });
            setPayments(response.data);
        } catch (error) {
            console.error('Error fetching payments', error);
        }
    };

    return (
        <div>
            <h2>Payments on {date}</h2>
            <input
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
            />
            <table>
                <thead>
                    <tr>
                        <th>Admission Number</th>
                        <th>Amount</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {payments.map((payment) => (
                        <tr key={payment.id}>
                            <td>{payment.admission_number}</td>
                            <td>{payment.amount}</td>
                            <td>{payment.date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PaymentsPerDay;
