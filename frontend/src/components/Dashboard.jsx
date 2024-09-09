import React, { useState, useEffect } from 'react';

function Dashboard() {
    const [issues, setIssues] = useState([]);

    useEffect(() => {
        fetch('/api/issues')
            .then(response => response.json())
            .then(data => setIssues(data));
    }, []);

    return (
        <div>
            <h1>Issue Tracking Dashboard</h1>
            <ul>
                {issues.map(issue => (
                    <li key={issue.id}>
                        {issue.type} detected at {issue.location}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Dashboard;
