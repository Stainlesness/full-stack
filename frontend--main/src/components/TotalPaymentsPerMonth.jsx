// src/components/TotalPaymentsPerMonth.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TotalPaymentsPerMonth = () => {
    const [month, setMonth] = useState('');
    const [total, setTotal] = useState(0);
    const [loading, setLoading] = useState(false); // Loading state
    const [error, setError] = useState(null); // Error state

    useEffect(() => {
        if (month) {
            fetchTotalPayments();
        } else {
            setTotal(0); // Reset total if no month is selected
        }
    }, [month]);

    const fetchTotalPayments = async () => {
        setLoading(true); // Set loading to true
        setError(null); // Reset any previous error
        try {
            const response = await axios.get(`https://back-end2-dl6sdah86-stanoos-projects.vercel.app/payments/total`, {
                params: { month }
            });
            setTotal(response.data.total || 0); // Set total or default to 0 if not found
        } catch (error) {
            console.error('Error fetching total payments', error);
            setError('Failed to fetch total payments. Please try again.'); // Set error message
        } finally {
            setLoading(false); // Set loading to false regardless of success or failure
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
            {loading ? (
                <p>Loading total payments...</p> // Loading message
            ) : error ? (
                <p>{error}</p> // Display error message if there was an error
            ) : (
                <p>Total Amount: {total > 0 ? total : 'No payments found for this month.'}</p> // Message if no payments
            )}
        </div>
    );
};

export default TotalPaymentsPerMonth;
