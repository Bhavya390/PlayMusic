import os
import MySQLdb
from sys import argv
db = MySQLdb.connect("localhost","root","","music")
cursor = db.cursor()

def display():
	sql4 = "SELECT * FROM play"
	try:
		
		cursor.execute(sql4)
		results = cursor.fetchall()
		for row in results:
			name = row[0]
			path = row[1]
			print "nameofsong = %s , songpath = %s" % \
					(name,path)
			

	except:
		print"Error:unable to fetch data"
def insert(name,filename):
	sql = "INSERT INTO play(Name, \
    	   Filepath) \
       	VALUES ('%s','%s')" % \
       	(name,filename)
	try:
		cursor.execute(sql)
		db.commit()
	
	except:
		db.rollback()

def select(fname):
	sql2 = "SELECT * FROM play"

	try:
		flag = 1
		cursor.execute(sql2)
		results = cursor.fetchall()
		for row in results:
			name = row[0]
			path = row[1]
			print "nameofsong = %s , songpath = %s" % \
					(name,path)
			if(fname == path):
				flag = 0
		return flag

	except:
		print"Error:unable to fetch data"



def main():
	script , filename = argv
	print "Till now Songs present in playlist"
	display()
	print "Would you like to listen to song from playlist Enter 1 or To insert song and listen Enter 2"
	r = raw_input("> ")
	if(r == "2"):
		name  = raw_input("nameofsong > ")
		print "The song which your are uploading %s" %filename
		s = select(filename)
		if(s):
			print "can insert the song in playlist "
			insert(name,filename)
		else:
			print "song is Already present"


		display()
		print "select song from above list and give nameofsong as input"
		player = raw_input()

		cursor.execute("SELECT Filepath FROM play WHERE name = %s ",(player))
		p = str(cursor.fetchone()[0])

		os.startfile(p)
	elif(r == "1"):
		display()
		print "select song from above list and give nameofsong as input"
		player = raw_input()

		cursor.execute("SELECT Filepath FROM play WHERE name = %s ",(player))
		p = str(cursor.fetchone()[0])

		os.startfile(p)

	db.close()
#to create a table in db 
#sql = """CREATE TABLE play(
#		Name TEXT(20),
#		Filepath varchar(20)
#	)"""
#cursor.execute(sql)
main()
