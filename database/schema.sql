CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE elections (
    election_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    created_by INT REFERENCES users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(user_id)
);

CREATE TABLE candidates (
    candidate_id SERIAL PRIMARY KEY,
    election_id INT REFERENCES elections(election_id),
    user_id INT REFERENCES users(user_id),
    name VARCHAR(100) NOT NULL,
    party VARCHAR(50),
    platform TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (election_id) REFERENCES elections(election_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE votes (
    vote_id SERIAL PRIMARY KEY,
    election_id INT REFERENCES elections(election_id),
    candidate_id INT REFERENCES candidates(candidate_id),
    voter_id INT REFERENCES users(user_id),
    voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (election_id, voter_id),
    FOREIGN KEY (election_id) REFERENCES elections(election_id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (voter_id) REFERENCES users(user_id)
);

CREATE INDEX idx_elections_start_date ON elections(start_date);
CREATE INDEX idx_elections_end_date ON elections(end_date);
CREATE INDEX idx_votes_voted_at ON votes(voted_at);