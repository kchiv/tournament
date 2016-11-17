# tournament

This is the project for the Intro to Relational Databases module in Udacity's Nanodegree program.

# Tournament Files

The tournament program consists of three files:

1. tournament.py - this contains all the scripts which make the swiss pairings
2. tournament.sql - this has all of the table data
3. tournament_test.py - this has all of the test scripts

# Starting the Vagrant Virtual Machine

Before creating your database you must start up your VM or virtual machine. Here is how you do that:
1. In your terminal, navigate to the /tournament directory then use the command ```vagrant up```
2. 


# Tournament Database

To create a tournament database and create the schema. 

There should be two tables in your database, one for player data and another with matches and match results.

Once the tables are set up you can run tournament_test.py and the output should be:

```
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```
