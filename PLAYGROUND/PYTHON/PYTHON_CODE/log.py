import filePopulation


# Log object, holds the date, odometer reading, amount of petrol and the price of petrol
class Log:
	def __init__(self, date, odometer, petrol, price):
		self.date = date
		self.dodmeter = odometer
		self.petrol = petrol
		self.price = price
		
# Takes in a new string and uses the filePopulation class to add the log to the specified file
#Takes in the file name, date, odometer reading, petrol, and the price
def newLog(fileName, date, odometer, petrol, price):
	l=date+'#'+odometer+'#'+petrol+'#'+price
	filePopulation.dataIn(fileName, l)

#obtains the first line of the specified file that holds the vehicle model of the user/file holder
#Takes in the file name for the log to be appended to
def getVehicleModel(fileName):
	lines=filePopulation.dataOut(fileName)
	return lines[0]

def getLogByDate(fileName, date):
	lines=filePopulation.dataOut(fileName)

#Returns all logs within a given file. 
#takes in an array/list of strings assumed to be attained from the dataOut function.
def getLogs(lines):
	v=[]
	for x in range(1, len(lines)):
		l=lines[x].split('#')
		temp = Log(l[0], l[1], l[2], l[3])
		v.append(temp)
	return v
