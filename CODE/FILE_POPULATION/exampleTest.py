import filePopulation

filePopulation.dataIn('test', 'hello world')

lines=filePopulation.dataOut('test')
for line in lines:
	print(line)
