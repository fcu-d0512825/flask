import sqlite3
from flask import Flask,render_template,g,request
app = Flask(__name__)
 
DATABASE = "test.db"
 
def connect_db():
	return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	if hasattr(g,'db'):
		g.db.close()


@app.route("/")
def index():
	c = g.db.cursor()
	cursor = c.execute('select BlockID,Nonce,TimeStamp,Data,Prehash,Hash from Blockchain')
    # convert query results into list to display
	colname = [d[0] for d in cursor.description]
	user_list = [ dict(zip(colname, r)) for r in cursor.fetchall()]
	count = len(user_list)
	return  render_template('index.html', c = user_list , count = count)

@app.route("/insert" ,methods=['GET','POST'])
def insert():
	if request.method == 'POST':
		ID = request.form['BlockID']
		nonce = request.form['Nonce']
		timeStamp = request.form['TimeStamp']
		data = request.form['Data']
		prehash = request.form['Prehash']
		hash = request.form['Hash']
		c = g.db.cursor()
		cursor = c.execute('select BlockID,Nonce,TimeStamp,Data,Prehash,Hash from Blockchain')
		# convert query results into list to display
		colname = [d[0] for d in cursor.description]
		user_list = [ dict(zip(colname, r)) for r in cursor.fetchall()]
		count = len(user_list)
		flag=""
		#check again
		if (user_list[count-1]['Hash'])== prehash and hash!='' and timeStamp!='' and int(ID)==int(count)+1:
			sql="INSERT INTO Blockchain(BlockID,Nonce,TimeStamp,Data,Prehash,Hash) VALUES ("+ ID + ',' + nonce + ',\'' + timeStamp + '\',\'' + data + '\',\'' + prehash + '\',\'' + hash + '\')'
			print(sql)
			cursor = c.execute(sql)
			g.db.commit()
		else:
			flag="Something Error"
			print(flag)
		#update
		cursor = c.execute('select BlockID,Nonce,TimeStamp,Data,Prehash,Hash from Blockchain')
		colname = [d[0] for d in cursor.description]
		user_list = [ dict(zip(colname, r)) for r in cursor.fetchall()]
		count = len(user_list)
		return  render_template('index.html', c = user_list , count = count , flag=flag)
	else:
		c = g.db.cursor()
		cursor = c.execute('select BlockID,Nonce,TimeStamp,Data,Prehash,Hash from Blockchain')
		colname = [d[0] for d in cursor.description]
		user_list = [ dict(zip(colname, r)) for r in cursor.fetchall()]
		count = len(user_list)
		flag=""
		return  render_template('index.html', c = user_list , count = count , flag=flag)
@app.route("/login")
	return render_template('login.html')
@app.route("/block")
def blockchain():
    return render_template('block.html')

@app.route("/testing")
def testing():
    return render_template('002.html')
@app.route("/hello")
def hello():
    return "Hello World"
if __name__ == "__main__":
    app.run()