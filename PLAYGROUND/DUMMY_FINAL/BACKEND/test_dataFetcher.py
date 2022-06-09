from select import select
import unittest
import dataFetcher

## There should be no user log files present when this test is run
class testCreate(unittest.TestCase):
    def test_exists(self):
        self.assertFalse(dataFetcher.fileExists("jeff"))
    def test_create(self):
        dataFetcher.createLog('greg', 'Petrol', 'Sudan')
        self.assertTrue(dataFetcher.fileExists('greg'))
    def test_addLogEntry(self):
        dataFetcher.addLogEntry('greg', '2020-21-01', 1234, 3.4)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
