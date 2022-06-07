#Takes in the name of the file (without the type) as a string, and a log as a string.
#Prints the log string to the file
def dataIn(fileName, log):
	with open(fileName+'.txt', 'a') as f:
		print(log, file=f)

#takes in the file name (without file type) 
#returns all logs present in the chosen file		
def dataOut(fileName):
	file1=open(fileName+'.txt', 'r+')
	logs=file1.readlines()
	return logs

#Takes in the name of the file (without the type) as a string, and a log as a string.
#Prints the log string to the file
def byteIn(fileName, log):
	with open(fileName+'.txt', 'ab') as f:
		f.write(log)
#takes in the file name (without file type) 
#returns all logs present in the chosen file		
def byteOut(fileName):
	file1=open(fileName+'.txt', 'r+b')
	logs=file1.readlines()
	return logs