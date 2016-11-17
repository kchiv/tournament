-- Table definitions for the tournament project.
--
-- Drop tournament DB exists
DROP DATABASE IF EXISTS tournament;

-- Create tournament DB
CREATE DATABASE tournament;

-- Connect to tournament DB
\connect tournament

-- Drop players table if exists
DROP TABLE IF EXISTS players;

-- Drop matches table if exists
DROP TABLE IF EXISTS matches;

-- Create players table
CREATE TABLE players (
	player_id serial PRIMARY KEY,
	player_name text
);

-- Create matches table
CREATE TABLE matches (
	match_id serial PRIMARY KEY,
	winner integer REFERENCES players(player_id),
	loser integer REFERENCES players(player_id)
);