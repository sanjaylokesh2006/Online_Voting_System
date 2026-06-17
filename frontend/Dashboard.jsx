import React, { useState } from 'react';
import { Button, Card, ListGroup } from 'react-bootstrap';

function Dashboard() {
  const [voters, setVoters] = useState([
    { id: 1, name: 'John Doe', voted: false },
    { id: 2, name: 'Jane Smith', voted: false },
    { id: 3, name: 'Alice Johnson', voted: false }
  ]);

  const handleVote = (id) => {
    setVoters(
      voters.map((voter) =>
        voter.id === id ? { ...voter, voted: true } : voter
      )
    );
  };

  return (
    <div className="Dashboard">
      <h2>Voting Dashboard</h2>
      <Card>
        <Card.Body>
          <Card.Title>List of Voters</Card.Title>
          <ListGroup variant="flush">
            {voters.map((voter) => (
              <ListGroup.Item key={voter.id}>
                {voter.name}
                {!voter.voted && (
                  <Button onClick={() => handleVote(voter.id)}>Vote</Button>
                )}
              </ListGroup.Item>
            ))}
          </ListGroup>
        </Card.Body>
      </Card>
    </div>
  );
}

export default Dashboard;