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

cursor = db.cursor()
record_insert = "INSERT INTO player (first_name, last_name, team_id ) VALUES (%s,%s,%s)"
record1 = ("Smeagol","Shire Folk",1)

cursor.execute(record_insert, (record1))

db.commit()

print("---Displaying Players After Insert ---")
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
for player in players:
   
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {} ".format(player[2]))
    print("Team Name: {} ".format(player[3]))
    print("\n")

cursor = db.cursor()
record_update = "UPDATE player SET team_id = 2, first_name = 'Gollum' , last_name = 'Ringstealer' WHERE first_name = 'Smeagol'"
cursor.execute(record_update)
db.commit()

print("---Displaying Players After Update ---")
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
for player in players:
   
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {} ".format(player[2]))
    print("Team Name: {} ".format(player[3]))
    print("\n")

cursor = db.cursor()
record_delete = "DELETE FROM player WHERE first_name = 'Gollum'"
cursor.execute(record_delete)
db.commit()

print("---Displaying Players After Delete ---")
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
for player in players:
   
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {} ".format(player[2]))
    print("Team Name: {} ".format(player[3]))
    print("\n")

#sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

#mycursor.execute(sql)