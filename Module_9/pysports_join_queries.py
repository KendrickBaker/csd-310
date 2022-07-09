import mysql.connector
from mysql.connector import errorcode 

config = {
    "user":"pysports_user",
    "password":"Goomba99j#",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

db = mysql.connector.connect(**config)

print("---Displaying Player Records ---")
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
for player in players:
   
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {} ".format(player[2]))
    print("Team Name: {} ".format(player[3]))
    print("\n")
