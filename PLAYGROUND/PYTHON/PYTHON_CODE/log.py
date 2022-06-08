import filePopulation


# Log object, holds the date, odometer reading, amount of petrol and the price of petrol
class Log:
	def __init__(self, date, odometer, petrol, price):
		self.date = date
		self.dodmeter = float(odometer)
		self.petrol = float(petrol)
		self.price = float(price)

class Date:
	def _init_(self, year, month, day):
		self.year = int(year)
		self.month = int(month)
		self.day = int(day)
		
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

#Returns all logs within a given file. 
#takes in an array/list of strings assumed to be attained from the dataOut function.
def getLogs(fileName):
	v=[]
	lines=filePopulation.dataOut(fileName)
	for x in range(1, len(lines)):
		l=lines[x].split('#')
		ds=l[0].split('-')
		d = Date(ds[0], ds[1], ds[2])
		temp = Log(d, l[1], l[2], l[3])
		v.append(temp)
	return v
	
def getLogByDate(fileName, date):
	logs=getLogs(fileName)
	ds=date.split('-')
	d=Date(ds[0], ds[1], ds[2])
	for x in range(1, len(logs)):
		if(x.date.year == d.year):
			if(x.date.month == d.month):
				if(x.date.day == d.day):
					return x
	
def getLogBetweenDates(fileName, startDate, endDate):
	v=[]
	logs=getLogs(fileName)
	dsStart=startDate.split('-')
	dsEnd=endDate.split('-')
	start=Date(dsStart[0], dsStart[1], dsStart[2])
	end = Date(dsEnd[0], dsEnd[1], dsEnd[2])
	for x in logs:
		if(x.date.year >= start.year & x.date.year <= end.year):
			if(x.date.month >= start.month & x.date.month <= end.month):
				if(x.date.day >= start.day & x.date.day <= end.day):
					v.append(x)
	return v