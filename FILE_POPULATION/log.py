import filePopulation

class Log:
	def __init__(self, date, odometer, petrol, price):
		self.date = date
		self.dodmeter = odometer
		self.petrol = petrol
		self.price = price

def newLog(fileName, date, odometer, petrol, price):
	l=date+'#'+odometer+'#'+petrol+'#'+price
	filePopulation.dataIn(fileName, l)

def getVehicleModel(fileName):
	lines=filePopulation.dataOut(fileName)
	return lines[0]

def getLogByDate(fileName, date):
	lines=filePopulation.dataOut(fileName)


def getLogs(lines):
	v=[]
	for x in range(1, len(lines)):
		v=lines[x].split('#')
