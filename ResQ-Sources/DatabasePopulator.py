import sqlite3,time
import DatabaseMapper as sqlasvoice
import DanceRobot
connection = sqlite3.connect("resq_table.db")
cursor = connection.cursor()

'''
command1 = """CREATE TABLE IF NOT EXISTS
resqmedicine(INDEX_ID INTEGER PRIMARY KEY AUTOINCREMENT,
USERNAME TEXT NOT NULL,
MEDICINE TEXT NOT NULL,
TIME INTEGER NOT NULL,
TYPE TEXT NOT NULL)"""

cursor.execute(command1)

'''

# DATABASE BACKEND CONTROLLER
update_agents = {0:"Admin",1:"Tuhinadri",2:"Aditya",3:"Walter"} # Mapped By ResQ Admin

'''
def add_to_database(name,medicine,time,timetype):
	
	#cursor.execute("INSERT INTO resqmedicine (USERNAME, MEDICINE, TIME, TYPE) VALUES ( 'Tuhinadri', 'Nescafe', 1, 'AM' )")  #--> INSERTING RECORDS	
	connection.commit()	
'''

def add_to_database(name,medicine,time,timetype):
	name = "'"+name+"'"
	medicine = "'"+medicine+"'"
	time = str(time)
	timetype = "'"+timetype+"'"
	cursor.execute("INSERT INTO resqmedicine (USERNAME, MEDICINE, TIME, TYPE) VALUES (" +name+","+medicine+","+time+","+timetype+ ")")  #--> INSERTING RECORDS
	connection.commit()



# END OF SQL UPDATE METHOD CREATION


# WEB-FRAMEWORK FOR INSERTION
from bottle import route, run, template, request

@route('/')
def index():
    return template('edit_task')

@route('/login')
def login():
    return '''
		<h2> ResQ Medicine Portal </h2>
        <form action="/login" method="post">
        <fieldset>
        <legend> Update Timings: </legend><br>            
            
			ID Number (1-3):<input list="ids" name="id">
			<datalist id="ids">
			<option value="1">
			<option value="2">
			<option value="3">
			</datalist><br>
            
            Medicine: <input name="medicine" type="text" /><br>
			Time (12Hrs): <input name="time" type="text" /><br>

			AM/PM:<input list="browsers" name="timetype">
			<datalist id="browsers">
			<option value="AM">
			<option value="PM">
			</datalist><br><br>            
            
            <input value="Update" type="submit" />
		</fieldset>
        </form>

        
    '''
#ID Number (1-3): <input name="id" type="text" /><br>
@route('/login', method='POST')
def do_login():
	name = request.forms.get('id')
	name = update_agents[int(name)]
	medicine = request.forms.get('medicine')
	time = request.forms.get('time')
	time = int(time)
	timetype = request.forms.get('timetype')
	# FETCHING THE POST REQUEST BEAN
	try:
		add_to_database(name,medicine,time,timetype)
		print(name,medicine,time,timetype)
		sqlasvoice.newentrysuccess("Database Updated")
		DanceRobot.nudgeyes()
		#return "<p>Your Records Have Been Added Successfully.</p>"
		return template('success')
	except:
		return "<p>Transaction Failed.</p>"


run(host='0.0.0.0', port=45000, debug = True)









