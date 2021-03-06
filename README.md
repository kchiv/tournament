# tournament

This is the project for the Intro to Relational Databases module in Udacity's Nanodegree program.

# Requirements

1. Python v2.7 installed
2. The latest vagrant build for the tournament project

# Tournament Files

The tournament program consists of three files:

1. tournament.py - this contains all the scripts which make the swiss pairings
2. tournament.sql - this has all of the table data
3. tournament_test.py - this has all of the test scripts

# Starting the Vagrant Virtual Machine

Before creating your database you must start up your VM or virtual machine. Here is how you do that:

1. In your terminal, navigate to the /tournament directory then use the command ```vagrant up```. This powers up the virtual machine.
2. You need to login to the virtual machine and you can do this by typing the command ```vagrant ssh```.

# Tournament Database

After you've started up the virtual machine and logged in, you will need to create a tournament database.

You can create a database as well as the schema by either running the SQL commands in your terminal or executing the commands in the tournament.sql.

To create a database in command line you must do the following:

1. Run the command ```psql``` in the terminal.
2. Next run the following commands to create the tournament database and connect to it.

```
vagrant@trusty32: vagrant => CREATE DATABASE tournament;
vagrant@trusty32: vagrant => \c tournament;
vagrant@trusty32: tournament =>
```

3. Once we have created the database and connected to it, we can then create tables in the terminal.
```
vagrant@trusty32: tournament => CREATE TABLE [table name](....);
```

As previously mentioned, you can also create the database and all the tables by executing a SQL file that has all the commands.

Here is how you can do that:

1. Run the command ```psql``` in the terminal.
2. Run the ```\i``` command or the import command on your SQL file.
```
vagrant@trusty32: psql => \i tournament.sql
```

# Testing the Program

Once the database and the tables are set up, you need to run tournament_test.py to make sure everything is working correctly.

To run the test script, you must navigate to the \tournament directory in your terminal, and then run the following command:

```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
```

If everything is working correctly you will get the following output:
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
