-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS nfl;

-- Usar la base de datos nfl
USE nfl;

-- Crear tabla teams si no existe
CREATE TABLE IF NOT EXISTS teams (
    team_id INT PRIMARY KEY AUTO_INCREMENT,
    team_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    stadium VARCHAR(100) NOT NULL,
    founded_year INT NOT NULL
);

-- Crear tabla players si no existe
CREATE TABLE IF NOT EXISTS players (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    position VARCHAR(10) NOT NULL,
    jersey_number INT NOT NULL,
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Crear tabla coaches si no existe
CREATE TABLE IF NOT EXISTS coaches (
    coach_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Crear tabla games si no existe
CREATE TABLE IF NOT EXISTS games (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    home_team_id INT,
    away_team_id INT,
    game_date DATE NOT NULL,
    home_team_score INT NOT NULL,
    away_team_score INT NOT NULL,
    FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id)
);

-- Crear tabla player_stats si no existe
CREATE TABLE IF NOT EXISTS player_stats (
    stat_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT,
    game_id INT,
    touchdowns INT NOT NULL,
    passing_yards INT NOT NULL,
    rushing_yards INT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- Crear tabla team_stats si no existe
CREATE TABLE IF NOT EXISTS team_stats (
    team_stat_id INT PRIMARY KEY AUTO_INCREMENT,
    team_id INT,
    game_id INT,
    total_yards INT NOT NULL,
    total_touchdowns INT NOT NULL,
    penalties INT NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);