from select import select
from turtle import distance
import unittest
import dataFetcher

## There should be no user log files present when this test is run
class testCreate(unittest.TestCase):
    def test_exists(self):
        self.assertFalse(dataFetcher.fileExists("jeff"))
    def test_saveAndRetreve(self):
        dataFetcher.createLog('greg', 'Petrol', 'Sudan')
        dataFetcher.addLogEntry('greg', '2020-01-01', 1234, 3.4)
        dataFetcher.addLogEntry('greg', '2020-01-02', 2234, 5.4)
        distance, energy, ave= dataFetcher.getLog('greg', '2021-01-02', '2022-01-01')
        self.assertEqual(distance, 1000)
        self.assertAlmostEqual(energy,513)
        self.assertAlmostEqual(ave,0.513)
    def test_discovery(self):
        dataFetcher.createLog('one', 'Petrol', 'SUV')
        dataFetcher.addLogEntry('one', '2020-01-01', 1234, 3.4)
        dataFetcher.addLogEntry('one', '2020-01-02', 2234, 5.4)
        dataFetcher.createLog('two', 'Petrol', 'Coupe')
        dataFetcher.addLogEntry('two', '2020-01-01', 1234, 3.4)
        dataFetcher.addLogEntry('two', '2020-01-02', 2234, 5.4)
        dataFetcher.createLog('three', 'Petrol', '4x4')
        dataFetcher.addLogEntry('three', '2020-01-01', 1234, 3.4)
        dataFetcher.addLogEntry('three', '2020-01-02', 2234, 5.4)
        print(dataFetcher.vehiclesWithFuelType('Petrol'))
        self.assertTrue(dataFetcher.vehiclesWithFuelType('Petrol').__contains__('4x4'))



if __name__ == '__main__':
    unittest.main()
