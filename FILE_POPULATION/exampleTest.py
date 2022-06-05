import log
import filePopulation

log.newLog('test', '05/03', '123', '12', '1')

lines = filePopulation.dataOut('test')

logs=log.getLogs(lines)

for x in logs:
	print(x.date)
