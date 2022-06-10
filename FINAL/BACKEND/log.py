import filePopulation
import datetime


# Log object, holds the date, distance reading, amount of petrol and the price of petrol
class Log:
	def __init__(self, date, odometer, distance, petrol, price):
		self.date = date
		self.odometer=float(odometer)
		self.distance = float(distance)
		self.petrol = float(petrol)
		self.price = float(price)
		
# Takes in a new string and uses the filePopulation class to add the log to the specified file
#Takes in the file name, date, distance reading, petrol, and the price
def newLog(fileName, date, odometer, petrol, price):
	lastLog = getlastLog(fileName)
	distance = 0
	if(lastLog != -1):
		distance = odometer - lastLog.odometer
	l=date+'#'+str(odometer)+'#'+str(distance)+'#'+str(petrol)+'#'+str(price)
	filePopulation.dataIn(fileName, l)

# returns the last log entry or -1 if there is no last log entry
def getlastLog(fileName):
	lines=filePopulation.dataOut(fileName)
	if(len(lines)>1):
		last = lines[len(lines)-1]
		return makeLog(last)
	else:
		return -1



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
		temp = makeLog(lines[x])
		v.append(temp)
	return v
def makeLog(line):
	l = line.split('#')
	ds=l[0].split('-')
	d = datetime.date(int(ds[0]), int(ds[1]), int(ds[2]))
	return Log(d,l[1], l[2], l[3], l[4])
	
def getLogByDate(fileName, date):
	logs=getLogs(fileName)
	ds=date.split('-')
	d=datetime.date(int(ds[0]), int(ds[1]), int(ds[2]))
	for x in logs:
		if(x.date == d):
			return x
			
	
def getLogsBetweenDates(fileName, startDate, endDate):
	v=[]
	logs=getLogs(fileName)
	dsStart=startDate.split('-')
	dsEnd=endDate.split('-')
	start = datetime.date(int(dsStart[0]), int(dsStart[1]), int(dsStart[2]))
	end = datetime.date(int(dsEnd[0]), int(dsEnd[1]), int(dsEnd[2]))
	for x in logs:
		if(x.date >= start and x.date <= end):
			v.append(x)
	return v