// src/components/TotalPaymentsPerMonth.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TotalPaymentsPerMonth = () => {
    const [month, setMonth] = useState('');
    const [total, setTotal] = useState(0);

    useEffect(() => {
        if (month) {
            fetchTotalPayments();
        }
    }, [month]);

    const fetchTotalPayments = async () => {
        try {
            const response = await axios.get(`https://back-end2-dl6sdah86-stanoos-projects.vercel.app/payments/total`, {
                params: { month }
            });
            setTotal(response.data.total);
        } catch (error) {
            console.error('Error fetching total payments', error);
        }
    };

    return (
        <div>
            <h2>Total Payments for {month}</h2>
            <input
                type="month"
                value={month}
                onChange={(e) => setMonth(e.target.value)}
            />
            <p>Total Amount: {total}</p>
        </div>
    );
};

export default TotalPaymentsPerMonth;
