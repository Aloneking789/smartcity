import React from 'react';

function IssueList({ issues }) {
    return (
        <div>
            <h2>Reported Issues</h2>
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

export default IssueList;
