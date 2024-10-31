from fastapi import APIRouter, HTTPException
from app.models import (TeamCreate, Team, PlayerCreate, Player, CoachCreate, Coach,GameCreate, Game, PlayerStatCreate, PlayerStat, TeamStatCreate, TeamStat)
from app.database import get_db_connection
from typing import List
from datetime import datetime

router = APIRouter()

# Team endpoints
@router.post("/teams/", response_model=Team, tags=["Teams"])
def create_team(team: TeamCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO teams (team_name, city, stadium, founded_year)
        VALUES (%s, %s, %s, %s)
        """
        values = (team.team_name, team.city, team.stadium, team.founded_year)
        
        cursor.execute(query, values)
        conn.commit()
        
        team_id = cursor.lastrowid
        return Team(team_id=team_id, **team.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/teams/", response_model=List[Team], tags=["Teams"])
def list_teams():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM teams"
        cursor.execute(query)
        teams = cursor.fetchall()
        return [Team(**team) for team in teams]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/teams/bulk/", response_model=List[Team], tags=["Teams"])
def create_teams_bulk(teams: List[TeamCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO teams (team_name, city, stadium, founded_year)
        VALUES (%s, %s, %s, %s)
        """
        values = [(t.team_name, t.city, t.stadium, t.founded_year) for t in teams]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        team_ids = range(last_id - len(teams) + 1, last_id + 1)
        
        return [Team(team_id=tid, **t.dict()) for tid, t in zip(team_ids, teams)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Player endpoints
@router.post("/players/", response_model=Player, tags=["Players"])
def create_player(player: PlayerCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO players (first_name, last_name, position, jersey_number, team_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (player.first_name, player.last_name, player.position, player.jersey_number, player.team_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        player_id = cursor.lastrowid
        return Player(player_id=player_id, **player.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/players/", response_model=List[Player], tags=["Players"])
def list_players():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM players"
        cursor.execute(query)
        players = cursor.fetchall()
        return [Player(**player) for player in players]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/players/bulk/", response_model=List[Player], tags=["Players"])
def create_players_bulk(players: List[PlayerCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO players (first_name, last_name, position, jersey_number, team_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = [(p.first_name, p.last_name, p.position, p.jersey_number, p.team_id) for p in players]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        player_ids = range(last_id - len(players) + 1, last_id + 1)
        
        return [Player(player_id=pid, **p.dict()) for pid, p in zip(player_ids, players)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
# Coach endpoints
@router.post("/coaches/", response_model=Coach, tags=["Coaches"])
def create_coach(coach: CoachCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO coaches (first_name, last_name, role, team_id)
        VALUES (%s, %s, %s, %s)
        """
        values = (coach.first_name, coach.last_name, coach.role, coach.team_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        coach_id = cursor.lastrowid
        return Coach(coach_id=coach_id, **coach.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/coaches/", response_model=List[Coach], tags=["Coaches"])
def list_coaches():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM coaches"
        cursor.execute(query)
        coaches = cursor.fetchall()
        return [Coach(**coach) for coach in coaches]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/coaches/bulk/", response_model=List[Coach], tags=["Coaches"])
def create_coaches_bulk(coaches: List[CoachCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO coaches (first_name, last_name, role, team_id)
        VALUES (%s, %s, %s, %s)
        """
        values = [(c.first_name, c.last_name, c.role, c.team_id) for c in coaches]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        coach_ids = range(last_id - len(coaches) + 1, last_id + 1)
        
        return [Coach(coach_id=cid, **c.dict()) for cid, c in zip(coach_ids, coaches)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Game endpoints
@router.post("/games/", response_model=Game, tags=["Games"])
def create_game(game: GameCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO games (home_team_id, away_team_id, game_date, home_team_score, away_team_score)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (game.home_team_id, game.away_team_id, game.game_date, game.home_team_score, game.away_team_score)
        
        cursor.execute(query, values)
        conn.commit()
        
        game_id = cursor.lastrowid
        return Game(game_id=game_id, **game.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/games/", response_model=List[Game], tags=["Games"])
def list_games():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM games"
        cursor.execute(query)
        games = cursor.fetchall()
        return [Game(**game) for game in games]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/games/bulk/", response_model=List[Game], tags=["Games"])
def create_games_bulk(games: List[GameCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO games (home_team_id, away_team_id, game_date, home_team_score, away_team_score)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = [(g.home_team_id, g.away_team_id, g.game_date, g.home_team_score, g.away_team_score) for g in games]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        game_ids = range(last_id - len(games) + 1, last_id + 1)
        
        return [Game(game_id=gid, **g.dict()) for gid, g in zip(game_ids, games)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# PlayerStat endpoints
@router.post("/player_stats/", response_model=PlayerStat, tags=["Player Stats"])
def create_player_stat(player_stat: PlayerStatCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO player_stats (player_id, game_id, touchdowns, passing_yards, rushing_yards)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (player_stat.player_id, player_stat.game_id, player_stat.touchdowns, 
                    player_stat.passing_yards, player_stat.rushing_yards)
        
        cursor.execute(query, values)
        conn.commit()
        
        stat_id = cursor.lastrowid
        return PlayerStat(stat_id=stat_id, **player_stat.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/player_stats/", response_model=List[PlayerStat], tags=["Player Stats"])
def list_player_stats():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM player_stats"
        cursor.execute(query)
        player_stats = cursor.fetchall()
        return [PlayerStat(**stat) for stat in player_stats]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/player_stats/bulk/", response_model=List[PlayerStat], tags=["Player Stats"])
def create_player_stats_bulk(player_stats: List[PlayerStatCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO player_stats (player_id, game_id, touchdowns, passing_yards, rushing_yards)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = [(ps.player_id, ps.game_id, ps.touchdowns, ps.passing_yards, ps.rushing_yards) for ps in player_stats]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        stat_ids = range(last_id - len(player_stats) + 1, last_id + 1)
        
        return [PlayerStat(stat_id=sid, **ps.dict()) for sid, ps in zip(stat_ids, player_stats)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# TeamStat endpoints
@router.post("/team_stats/", response_model=TeamStat, tags=["Team Stats"])
def create_team_stat(team_stat: TeamStatCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO team_stats (team_id, game_id, total_yards, total_touchdowns, penalties)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (team_stat.team_id, team_stat.game_id, team_stat.total_yards, 
                team_stat.total_touchdowns, team_stat.penalties)
        
        cursor.execute(query, values)
        conn.commit()
        
        team_stat_id = cursor.lastrowid
        return TeamStat(team_stat_id=team_stat_id, **team_stat.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/team_stats/", response_model=List[TeamStat], tags=["Team Stats"])
def list_team_stats():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM team_stats"
        cursor.execute(query)
        team_stats = cursor.fetchall()
        return [TeamStat(**stat) for stat in team_stats]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/team_stats/bulk/", response_model=List[TeamStat], tags=["Team Stats"])
def create_team_stats_bulk(team_stats: List[TeamStatCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO team_stats (team_id, game_id, total_yards, total_touchdowns, penalties)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = [(ts.team_id, ts.game_id, ts.total_yards, ts.total_touchdowns, ts.penalties) for ts in team_stats]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        stat_ids = range(last_id - len(team_stats) + 1, last_id + 1)
        
        return [TeamStat(team_stat_id=sid, **ts.dict()) for sid, ts in zip(stat_ids, team_stats)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


#querys

@router.get("/Query1/", tags=["Query1: Get player stats by game id"])
def get_player_stats_by_game_id(game_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM player_stats WHERE game_id = {game_id}"
        cursor.execute(query)
        player_stats = cursor.fetchall()
        return [PlayerStat(**stat) for stat in player_stats]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query2/", tags=["Query2: Get team stats by game id"])
def get_team_stats_by_game_id(game_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM team_stats WHERE game_id = {game_id}"
        cursor.execute(query)
        team_stats = cursor.fetchall()
        return [TeamStat(**stat) for stat in team_stats]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query3/", tags=["Query3: Get all games by team id"])
def get_all_games_by_team_id(team_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM games WHERE home_team_id = {team_id} OR away_team_id = {team_id}"
        cursor.execute(query)
        games = cursor.fetchall()
        return [Game(**game) for game in games]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query4/", tags=["Query4: Get all players by team id"])
def get_all_players_by_team_id(team_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM players WHERE team_id = {team_id}"
        cursor.execute(query)
        players = cursor.fetchall()
        return [Player(**player) for player in players]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query5/", tags=["Query5: Get all coaches by team id"])
def get_all_coaches_by_team_id(team_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM coaches WHERE team_id = {team_id}"
        cursor.execute(query)
        coaches = cursor.fetchall()
        return [Coach(**coach) for coach in coaches]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

from fastapi import FastAPI, HTTPException
from typing import List, Optional
import mysql.connector

router = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="nfl"
    )