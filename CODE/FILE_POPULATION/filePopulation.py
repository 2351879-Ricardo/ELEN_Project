
#Takes in the name of the file (without the type) as a string, and a log as a string.
#Prints the log string to the file
def dataIn(fileName, log):
	with open(fileName+'.txt', 'w') as f:
		print(log, file=f)

#takes in the file name (without file type) 
#returns all logs present in said file		
def dataOut(fileName):
	file1=open(fileName+'.txt', 'w')
	logs=file1.readlines()
	return logs

