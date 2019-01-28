import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
#----- create table -----
#c.execute('''CREATE TABLE Blockchain
'''      (BlockID INT PRIMARY KEY     NOT NULL,
       Nonce           INT    NOT NULL,
	   TimeStamp		TEXT	NOT NULL,
       Data            TEXT,
       Prehash        CHAR(64) NOT NULL,
'''#       Hash         CHAR(64)		NOT NULL);''')

#----- insert value -----
'''
c.execute("INSERT INTO Blockchain(BlockID,Nonce,TimeStamp,Data,Prehash,Hash) \
      VALUES (1, 35230,DateTime('now','localtime'),'', '0000000000000000000000000000000000000000000000000000000000000000', '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf' )");	  
conn.commit()
c.execute("INSERT INTO Blockchain(BlockID,Nonce,TimeStamp,Data,Prehash,Hash) \
      VALUES (2, 11316,DateTime('now','localtime'),'', '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf', '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19' )");	  
conn.commit()
c.execute("INSERT INTO Blockchain(BlockID,Nonce,TimeStamp,Data,Prehash,Hash) \
      VALUES (3, 12937,DateTime('now','localtime'),'', '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19', '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf' )");	  
conn.commit()
'''
#----- drop table -----

#c.execute("DROP TABLE Blockchain")

#----- update table -----
#c.execute("UPDATE Blockchain set Hash = '0000f961b07aaf61124011e3f673c18ce9d210f9fab62f7128c899d3f67dc86c' where BlockID=3")
#c.execute("UPDATE Blockchain set Prehash = '000029b999071c0c2799fd03c07bbf0c15ae97450c19c476975f60d959ae8bee' where BlockID=3")
#c.execute("UPDATE Blockchain set Nonce = 4616 where BlockID=3")
#conn.commit()

#----- delete value -----


c.execute("DELETE from Blockchain where BlockID=4")
c.execute("DELETE from Blockchain where BlockID=5")
c.execute("DELETE from Blockchain where BlockID=6")
c.execute("DELETE from Blockchain where BlockID=7")
conn.commit()

#----- select -----

cursor = c.execute('select BlockID,Nonce,TimeStamp,Data,Prehash,Hash from Blockchain')
values = c.fetchall()
for row in values:
	print("Block = ",row[0])
	print("Nonce = ",row[1])
	print("TimeStamp = ",row[2])
	print("Data = ",row[3])
	print("Prehash = ",row[4])
	print("Hash = ",row[5],"\n")
	
	
	


c.close()
conn.close()