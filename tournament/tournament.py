#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print "Connection failed!"

@contextmanager
def get_cursor():
    """
    Query helper function using context lib. Creates a cursor from a database
    connection object and perfors queries using that cursor.
    """
    db = connect()
    db_cursor = db.cursor()
    try:
        yield db_cursor
    except:
        raise
    else:
        db.commit()
    finally:
        db_cursor.close()
        db.close()


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM matches")


def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM players")


def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as cursor:
        cursor.execute("SELECT COUNT(player_id) FROM players")
        player_cnt = cursor.fetchone()[0]
        return player_cnt


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as cursor:
        query = "INSERT INTO players (player_name) VALUES (%s)"
        cursor.execute(query, (name,))

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as cursor:
        query = """
        SELECT players.player_id, players.player_name, (SELECT COUNT(matches.winner)
        FROM matches WHERE players.player_id = matches.winner) AS wins,
        (SELECT COUNT(matches.match_id) FROM matches WHERE
        players.player_id = matches.winner OR players.player_id = matches.loser)
        AS matches_played FROM players LEFT JOIN matches ON
        players.player_id = matches.winner GROUP BY players.player_id
        ORDER BY wins DESC
        """
        cursor.execute(query)
        player_st = cursor.fetchall()
        return player_st

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as cursor:
        query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
        cursor.execute(query, (winner, loser))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    with get_cursor() as cursor:
        query = """
        SELECT players.player_id, players.player_name, (SELECT COUNT(matches.winner)
        FROM matches WHERE players.player_id = matches.winner) AS wins,
        (SELECT COUNT(matches.match_id) FROM matches WHERE
        players.player_id = matches.winner OR players.player_id = matches.loser)
        AS matches_played FROM players LEFT JOIN matches ON
        players.player_id = matches.winner GROUP BY players.player_id
        ORDER BY wins DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        if countPlayers() < 2:
            print "There aren't enough players."
        else:
            i = 0
            pairings = []
            while i < len(rows):
                player_one_id = rows[i][0]
                player_one_name = rows[i][1]
                player_two_id = rows[i + 1][0]
                player_two_name = rows[i + 1][1]
                pairings.append((
                    player_one_id,
                    player_one_name,
                    player_two_id,
                    player_two_name))
                i = i + 2

            return pairings

